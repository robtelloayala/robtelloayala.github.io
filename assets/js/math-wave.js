import {
  BufferGeometry,
  Float32BufferAttribute,
  LineSegments,
  OrthographicCamera,
  Scene,
  ShaderMaterial,
  WebGLRenderer,
} from './vendor/three/three.module.js';

const banner = document.querySelector('.profile-math-banner');
if (banner) initializeWave(banner);

function initializeWave(element) {
  const canvas = element.querySelector('canvas');
  const toggle = element.querySelector('.wave-motion-toggle');
  const icon = toggle.querySelector('i');
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  let renderer;
  let scene;
  let camera;
  let material;
  let failed = false;
  let visible = false;
  let paused = false;
  let frame = null;
  let previousTime = null;
  let elapsed = 0;

  function stop() {
    if (frame !== null) cancelAnimationFrame(frame);
    frame = null;
    previousTime = null;
  }

  function showFallback() {
    stop();
    element.classList.remove('wave-ready');
    toggle.hidden = true;
  }

  function createScene() {
    const context = canvas.getContext('webgl2', { alpha: true, antialias: true, powerPreference: 'low-power' });
    if (!context) return false;
    renderer = new WebGLRenderer({ canvas, context, alpha: true, antialias: true });
    renderer.setClearColor(0xffffff, 0);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
    scene = new Scene();
    camera = new OrthographicCamera(-10.5, 10.5, 5.2, -5.2, 0.1, 100);
    const azimuth = 40 * Math.PI / 180;
    const elevation = 29 * Math.PI / 180;
    camera.up.set(0, 0, 1);
    camera.position.set(
      30 * Math.sin(azimuth) * Math.cos(elevation),
      30 * Math.cos(azimuth) * Math.cos(elevation),
      30 * Math.sin(elevation),
    );
    camera.lookAt(0, 0, 0);

    // Quad grid edges only, without the diagonals of a triangle wireframe.
    const vertices = [];
    const columns = 120;
    const rows = 96;
    for (let row = 0; row <= rows; row++) {
      for (let column = 0; column <= columns; column++) {
        const x = -10 + column / columns * 20;
        const y = -8 + row / rows * 16;
        if (column < columns) vertices.push(x, y, 0, x + 20 / columns, y, 0);
        if (row < rows) vertices.push(x, y, 0, x, y + 16 / rows, 0);
      }
    }
    const geometry = new BufferGeometry();
    geometry.setAttribute('position', new Float32BufferAttribute(vertices, 3));
    material = new ShaderMaterial({
      transparent: true,
      depthWrite: false,
      depthTest: false,
      uniforms: { time: { value: 0 } },
      vertexShader: `
        uniform float time;
        varying float height;
        varying float opacity;
        void main() {
          vec2 point = position.xy;
          float radius = length(point);
          float envelope = exp(-dot(point, point) / 28.0);
          // Slow angular drift of the wave, returning to the supplied function at t=0.
          float angle = 0.14 * sin(time * 0.055) * exp(-radius * radius / 90.0);
          mat2 rotation = mat2(cos(angle), -sin(angle), sin(angle), cos(angle));
          vec2 wave = rotation * point;
          height = envelope * sin(wave.x + time * 0.075) * cos(wave.y - time * 0.045);
          float edge = 1.0 - smoothstep(4.5, 8.0, radius);
          opacity = (0.06 + 0.48 * envelope) * edge;
          gl_Position = projectionMatrix * modelViewMatrix * vec4(point, height * 3.0, 1.0);
        }
      `,
      fragmentShader: `
        varying float height;
        varying float opacity;
        void main() {
          vec3 teal = vec3(0.196, 0.545, 0.569);
          vec3 blue = vec3(0.349, 0.431, 0.627);
          vec3 color = mix(teal, blue, clamp((height + 0.93) / 1.86, 0.0, 1.0));
          gl_FragColor = vec4(color, opacity);
        }
      `,
    });
    const surface = new LineSegments(geometry, material);
    surface.frustumCulled = false;
    scene.add(surface);

    canvas.addEventListener('webglcontextlost', () => {
      failed = true;
      showFallback();
    });
    return true;
  }

  function resize() {
    if (!renderer || failed) return;
    renderer.setSize(element.clientWidth, element.clientHeight, false);
    renderer.render(scene, camera);
  }

  function animate(now) {
    frame = requestAnimationFrame(animate);
    if (previousTime === null) previousTime = now;
    const delta = now - previousTime;
    if (delta < 1000 / 30) return;
    elapsed += Math.min(delta, 100) / 1000;
    previousTime = now;
    material.uniforms.time.value = elapsed;
    renderer.render(scene, camera);
  }

  function update() {
    if (reducedMotion.matches || failed) {
      showFallback();
      return;
    }
    if (!visible || document.hidden) {
      stop();
      return;
    }
    if (!renderer) {
      try {
        if (!createScene()) {
          failed = true;
          return;
        }
        resize();
      } catch {
        failed = true;
        showFallback();
        return;
      }
    }
    element.classList.add('wave-ready');
    toggle.hidden = false;
    if (paused) stop();
    else if (frame === null) frame = requestAnimationFrame(animate);
  }

  toggle.addEventListener('click', () => {
    paused = !paused;
    const label = paused ? 'Resume wave animation' : 'Pause wave animation';
    toggle.setAttribute('aria-label', label);
    toggle.title = label;
    icon.className = paused ? 'fas fa-play' : 'fas fa-pause';
    update();
  });
  new IntersectionObserver(([entry]) => {
    visible = entry.isIntersecting;
    update();
  }).observe(element);
  new ResizeObserver(resize).observe(element);
  reducedMotion.addEventListener('change', update);
  document.addEventListener('visibilitychange', update);
}
