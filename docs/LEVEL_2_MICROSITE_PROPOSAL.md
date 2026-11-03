# Architectural Proposal: Level 2 Interactive 3D Microsite
## "GIÁO // AFTER HOURS — The Living Diorama in WebGL"

**Document ID:** `docs/LEVEL_2_MICROSITE_PROPOSAL.md`  
**Target Profile:** Phan Văn Toàn (`@givoxxs` / "Giáo")  
**Project:** GitHub Profile README Redesign (Phase 2B)  
**Date:** 2026-11-03  
**Status:** PROPOSED ARCHITECTURAL BLUEPRINT (Zero Implementation in Phase 2B · Ready for Phase 3)

---

## 1. Executive Summary & Vision Manifesto

### 1.1 The Concept
While the GitHub Profile README (Level 1) delivers an accessible, high-contrast, mobile-responsive visual gateway, the **Level 2 Interactive 3D Microsite** expands Phan Văn Toàn's personal brand into a fully realized WebGL spatial world: **"GIÁO // AFTER HOURS — The Living Diorama in WebGL"**.

Floating high above the midnight waters of Da Nang Bay, the microsite renders a 30° axonometric diorama platform where Toàn's multidisciplinary engineering universe comes alive. Visitors navigate beyond static screenshots into an explorable simulation studio. They can inspect flight trajectory coordinates of an autonomous nano-drone, interactively manipulate a teacher-student prompt distillation graph, examine real-time edge computer vision inference topology on an infant crib, step directly inside a 1:20 scale graduation memory room, and travel alongside an autonomous robotic companion—**KURA-MK1**—who reacts with physical gestures and expressive emotional states.

### 1.2 Core Design Principles
1. **Zero Fake Sci-Fi Telemetry**: Every interactive element, coordinate graph, and telemetry readout maps directly to verified engineering research (ROS 2 Humble, NVIDIA Isaac Sim, Crazyflie 2.1 / GAP8 micro-UAVs, MediaPipe 33-point skeletal landmarking, and Claude Haiku → Gemma 4-26B prompt mutation loops).
2. **Deep Cultural Resonance**: Grounded in late-night Da Nang at 02:30 AM ("After Hours"). Features the golden arches of the Dragon Bridge (Cầu Rồng) reflecting across the Han River, ambient coastal rain audio, and an interactive dripping Vietnamese phin coffee.
3. **Rigorous Web Performance**: 60 FPS guaranteed across both modern desktop and mobile browsers via Meshopt/KTX2 compression, rigid asset budgets (<= 3.5 MB 3D assets, <= 4.5 MB initial page payload), and an unshakeable 4-tier progressive degradation ladder falling back to 2.5D CSS parallax where WebGL is restricted.

---

## 2. Scope Boundaries: Level 1 vs. Level 2

To maintain engineering discipline and prevent feature creep, a strict boundary separates Level 1 from Level 2.

```
+----------------------------------------------------------------------------------------------------+
|                                    LEVEL 1 vs LEVEL 2 SCOPE MATRIX                                 |
+------------------------------------+--------------------------------+------------------------------+
| Dimension                          | Level 1: GitHub Profile README | Level 2: Interactive 3D WebGL|
+------------------------------------+--------------------------------+------------------------------+
| Hosting & Execution Platform       | GitHub.com Web / Mobile App    | Standalone URL (Vercel Edge) |
| Runtime Technologies               | Static Markdown, HTML5, WebP   | Next.js 15, R3F, Three.js    |
| Interactivity Model                | Native hyperlinks & <details>  | 3D OrbitControls, Raycasting |
| Spatial Dimension                  | 2D Flat Responsive Layout      | Real-time 3D Axonometric Mesh|
| Asset Weight Budget                | <= 1.2 MB Total Static Assets  | <= 4.5 MB Total Initial Load |
| Robot Companion (KURA-MK1)         | Clean Static Visual Poses      | Rigged 3D Character & IK     |
| Audio & Atmosphere                 | None (Platform restriction)    | Spatial Web Audio API        |
| Phase 2B Implementation Status     | ACTIVE IMPLEMENTATION (M2)     | ARCHITECTURAL BLUEPRINT ONLY |
+------------------------------------+--------------------------------+------------------------------+
```

### 2.1 Strict Scope Enforcement Rule
> **MANDATE**: In Phase 2B, **no microsite source code, npm dependencies, or 3D asset bundles shall be built or added to the repository**. Milestone 2 is strictly committed to shipping the accessible GitHub Profile README (`README.md`) and establishing this definitive architectural proposal document. The implementation of Level 2 is scheduled for Phase 3.

---

## 3. Spatial Architecture & 3D Environment

The 3D environment is structured as a floating cutaway diorama island viewed through an isometric-style orthographic-perspective hybrid camera.

```
                                  [MIDNIGHT BACKGROUND PANORAMA]
                  Velvety Midnight Indigo Da Nang Bay Sky (#0B132B → #1C2541)
              Son Tra Peninsula Mountain Silhouettes · Low Coastal Mist Particles
           Golden Illuminated Dragon Bridge (Cầu Rồng) Arcing Across Han River
              Dynamic Water Shader with Planar Specular Reflections & Wave Ripple
    ═══════════════════════════════════════════════════════════════════════════════════════
                                                │
         [TIER 3: NORTH-WEST ELEVATED]          │          [TIER 2: NORTH-EAST RAISED]
         ZONE 1: SKILLS DISTILLATION            │          ZONE 3: BABYCARE AI
     - Dual Vertical CRT/OLED Displays          │      - 1:12 Scandinavian Birch Crib
     - Interactive Prompt Distillation Tree     │      - Articulated Overhead Camera Arm
     - Haiku → Gemma 4-26B Interactive Slider   │      - 33-Point MediaPipe Skeletal Mesh
     - +23.6% Accuracy Telemetry HUD            │      - Sub-50ms Edge Latency Profiler
    ────────────────────────────────────────────┴───────────────────────────────────────
                                [TIER 1: CENTRAL SUNKEN RUNWAY]
                                ZONE 2: ROBOTICS SIMULATION RIG
                        - Bead-blasted Stainless Runway (Z: -40mm)
                        - 3D Crazyflie 2.1 Nano-Drone (GAP8 Deck)
                        - Physics Trajectory Splines (Lemniscate / Helix)
                        - ROS 2 Humble / Isaac Sim Coordinate Inspector
    ────────────────────────────────────────────┬───────────────────────────────────────
         [TIER 2: SOUTH-WEST WORKBENCH]         │          [TIER 1: SOUTH-EAST DECK]
         ZONE 4: THE GIÁO ARCHIVE               │          KURA-MK1 & DA NANG CULTURE
     - 1:20 Scale Graduation Room Cutaway Box   │      - KURA-MK1 Interactive Droid
     - Interactive Brass Desk Lamp Switch       │      - Dripping Phin Iced Coffee Glass
     - Clickable Memory Corkboard Polaroids     │      - Lush Coastal Da Nang Succulent
     - Camera Fly-in Transition to WebGL Room   │      - Backlit Studio Nameplate:
                                                │        "GIÁO // AFTER HOURS"
    ═══════════════════════════════════════════════════════════════════════════════════════
                             [EXPOSED ARCHITECTURAL UNDERCARRIAGE]
       Oiled American Walnut (45mm) · CNC Chamfered Anodized Aluminum Chassis (Z: -120mm)
         Bundled Fiber Conduits · Copper Grounding Busbars · Cast Contact Shadows
```

### 3.1 Spatial Coordinates & Tier Hierarchy
The diorama island measures $2400\,\text{mm} \times 1600\,\text{mm}$ in virtual space, organized into four physical elevations:
- **Runway Level (Z: -40mm)**: Recessed central testing ground for micro-drone flight kinematics and coordinate calibration grids.
- **Main Deck (Z: 0mm)**: The primary walnut platform housing KURA-MK1, coffee station, and structural riser.
- **South-West Terrace (Z: +40mm)**: Elevated workbench dedicated to *The Giáo Archive* graduation room box.
- **North Tiers (Z: +80mm)**: Dual raised cantilevered platforms for *Skills Distillation* (North-West) and *BabyCare AI* (North-East).

### 3.2 Atmosphere & Dynamic Time-of-Day Duality
The microsite features a real-time environment toggle in the header HUD:
1. **"After Hours" (02:30 AM — Default)**:
   - Deep indigo sky (`#0B132B`) with soft Han river mist particles.
   - Dual 2700K amber brass desk lamps casting radial pools of warm light across dark walnut surfaces.
   - Golden illumination along the Dragon Bridge arches reflected in the river.
   - High-contrast luminescent cyan (`#38BDF8`) and mint (`#34D399`) vector telemetry lines.
2. **"First Light / Dawn Arrival" (06:00 AM)**:
   - Soft pastel gradient sky (apricot gold `#FED7AA` horizon bleeding into periwinkle blue `#E0F2FE`).
   - Morning sun directional light (5500K) washing across the studio from the East at a low 15° angle.
   - Monitor terminals automatically switch to crisp, high-contrast light mode UI themes.
   - KURA-MK1 enters Standby / Cat-loaf sleep mode beside the dripping coffee glass.

### 3.3 Han River Water Shader & Volumetric Lighting
- **Water Shader (`HanRiverWaterMaterial`)**: Custom GLSL shader with 2 octaves of Gerstner wave displacement, normal map blending, and Fresnel-driven planar reflection capturing the golden lights of the Dragon Bridge.
- **Lighting Rig**:
  - `KeyLightEast`: Directional light (`#FCD34D`, intensity 1.2) casting soft contact shadows (PCFSoftShadowMap, 1024x1024).
  - `DeskSpotWest`: SpotLight (2700K `#F59E0B`, angle 42°, penumbra 0.7, distance 1.8m) illuminating Zone 1 & Zone 4.
  - `DeskSpotEast`: SpotLight (2700K, angle 40°, penumbra 0.6) illuminating Zone 2 & KURA-MK1.
  - `AmbientFill`: AmbientLight (`#1E293B`, intensity 0.35) maintaining shadow detail without washed-out blacks.

---

## 4. The Four Interactive Project Workbenches (Zones)

Every interactive zone provides two layers of engagement: **In-Scene Hover/Click Interactivity** and **Detailed Telemetry Modal Overlays**.

```
+----------------------------------------------------------------------------------------------------+
|                                    PROJECT WORKBENCH SPECIFICATIONS                                |
+----------------------+-----------------------------+-----------------------------------------------+
| Zone                 | 3D Object Anchor            | Core Interactive Feature                      |
+----------------------+-----------------------------+-----------------------------------------------+
| 1. Skills            | Dual Vertical 27" Displays  | Interactive Prompt Tree & Haiku-Gemma Slider  |
|    Distillation      | on Articulated VESA Mount   | Live +23.6% convergence telemetry HUD         |
+----------------------+-----------------------------+-----------------------------------------------+
| 2. Robotics          | Crazyflie 2.1 Nano-Drone on | Orbital Trajectory Selector (Lemniscate/Helix)|
|    Simulation        | Twin-Axis Calibration Rig   | ROS 2 / Isaac Sim 50Hz Coordinate Inspector   |
+----------------------+-----------------------------+-----------------------------------------------+
| 3. BabyCare AI       | 1:12 Birch Nursery Crib &   | 33-Point MediaPipe 3D Landmark Mesh Overlay   |
|                      | Overhead Edge Camera Arm    | Real-time Sub-50ms Latency Profiler Breakdown |
+----------------------+-----------------------------+-----------------------------------------------+
| 4. The Giáo          | 1:20 Cutaway Room Box with  | Camera Fly-In Transition into 3D Room Box     |
|    Archive           | Glowing Brass Gooseneck Lamp| Functional Lamp Switch & Polaroid Memory Pins |
+----------------------+-----------------------------+-----------------------------------------------+
```

### 4.1 Zone 1: Skills Distillation (Prompt Engineering & SLM Optimization Desk)
- **Physical Setup**: Elevated North-West platform. Dual vertical monitors, walnut desk, mechanical keyboard, physical `SKILL.md` specification binder with yellow highlighter markings.
- **Interactive Experience**:
  - **Camera Glide**: Clicking the workbench smoothly translates and rotates the camera to an eye-level terminal view ($[-0.6, 1.2, 0.4]$, target $[-0.7, 0.9, -0.3]$).
  - **Interactive Prompt Lattice (Left Display)**: An interactive node graph rendered via SVG canvas texture. Visitors can click on prompt iterations (`v1_baseline` → `v2_semantic_pruning` → `v3_few_shot_distillation`) to inspect line-by-line diffs and automated Judge scoring.
  - **Teacher → Student Compression Slider (Right Display)**: An interactive HTML-in-3D range slider. Dragging from *Claude Haiku 4.5 (Teacher)* to *Gemma 4-26B (Student)* interactively plots token compression ratio (6.2x reduction), latency drops (from 820ms to 110ms), and accuracy delta (+23.6% peak, +17.2% average).
  - **Direct Actions**:
    - `[Launch Live Thesis App ↗]` (`https://skills-distillation.vercel.app`)
    - `[Inspect GitHub Repository ↗]` (`https://github.com/givoxxs/Skills_Distillation`)

### 4.2 Zone 2: Autonomous Flight Rig (Robotics Simulation & Digital Twins)
- **Physical Setup**: Central sunken runway. Carbon-fiber Crazyflie 2.1 nano-drone with GAP8 AI deck mounted on an articulated dual-ring calibration gimbal. Floor laser-etched with 50mm grids and AprilTags.
- **Interactive Experience**:
  - **Camera Glide**: Focuses camera into dynamic 3/4 perspective over the runway ($[0.0, 0.8, 0.6]$, target $[0.0, 0.4, 0.0]$).
  - **Physics Trajectory Switcher**: Clickable 3D buttons toggle animated cyan vector splines:
    1. *Figure-8 Lemniscate*: $x(t) = a \sin(t), y(t) = a \sin(t)\cos(t), z(t) = h + b \cos(2t)$ with animated velocity vectors and coordinate waypoints (`wp_01` to `wp_08`).
    2. *Ascending Helix*: $x(t) = r \cos(t), y(t) = r \sin(t), z(t) = ct$ with altitude contour rings.
    3. *Hover Perturbation*: Simulates synthetic wind gusts with real-time IMU PID error correction.
  - **ROS 2 & Isaac Sim Coordinate Inspector**: Floating HUD panel displaying:
    - Orientation: Quaternion $[q_w: 0.707, q_x: 0.000, q_y: 0.000, q_z: 0.707]$
    - Active Topics: `/crazyflie/odom [50 Hz]`, `/cmd_vel [100 Hz]`, `/gap8/optical_flow [30 Hz]`
    - Frame rate: 60 FPS in Isaac Sim synthetic physics engine.
  - **Action**: `[Inspect Simulation Packages ↗]` (`https://github.com/givoxxs`)

### 4.3 Zone 3: Autonomous Perception (BabyCare AI - Edge Computer Vision)
- **Physical Setup**: North-East raised birch terrace. Miniature 1:12 crib with soft fabric mattress, overhead articulated camera arm with optical glass lens and mint-green status LED.
- **Interactive Experience**:
  - **Camera Glide**: Elevates to an overhead oblique nursery angle ($[0.7, 1.1, 0.2]$, target $[0.6, 0.8, -0.4]$).
  - **33-Point MediaPipe 3D Landmark Mesh**: Toggling the overlay projects 33 luminous interconnected spherical nodes onto the infant mattress, tracing real-world MediaPipe topology (nose, eyes, shoulders, elbows, wrists, spine, hips, knees, ankles).
  - **Posture Morphing Selector**: Users select posture tabs ("Supine / Safe", "Prone / Alert", "Rollover / Warning"). The 3D landmark mesh smoothly morphs vertex positions, and the classification badge updates in real time (`SUPINE_SAFE (98.4%)` → `PRONE_HAZARD (96.1%)`).
  - **Edge Latency Profiler Widget**: An interactive waterfall chart showing real-time execution times:
    - Frame Capture: 4.2ms
    - MediaPipe Landmark Inference: 28.1ms
    - XGBoost Pose Classifier: 3.4ms
    - RTSP Stream Encoding: 6.3ms
    - **Total Pipeline Latency: 42.0ms** (Under 50ms real-time edge SLA).
  - **Action**: `[View BabyCare CV Repository ↗]` (`https://github.com/givoxxs/baby_posture_analysis`)

### 4.4 Zone 4: The Creative Spatial Archive (The Giáo Archive)
- **Physical Setup**: South-West workbench. An exquisite 1:20 scale cutaway architectural room box representing Toàn's iconic graduation room from `the-giao-archive.vercel.app`. Contains miniature desk, swivel chair, graduation gift box with salmon-orange ribbon, and photo corkboard.
- **Interactive Experience**:
  - **Camera Fly-In Transition**: Clicking the room box triggers a cinematic camera zoom that smoothly travels *through* the cutaway opening into the interior of the miniature room.
  - **Interactive Desk Lamp Switch**: Clicking the tiny gooseneck lamp on the desk triggers the audio click of an authentic toggle switch, dynamically transitioning the room from ambient dusk to a warm 2700K golden interior glow.
  - **Graduation Memory Pins**: Clicking pinned polaroid photos on the corkboard opens high-resolution modal memories (DUT university friends, DevDay 2026 award moment, hackathon late-night sessions).
  - **Seamless WebGL Portal**: Floating CTA button: `[Enter Fullscreen WebGL Chamber ↗]` opening `https://the-giao-archive.vercel.app/` with matched camera angles.

---

## 5. KURA-MK1 Guide Companion Architecture

KURA-MK1 (蔵) is not a decorative prop; it is an intelligent, physics-aware 3D companion agent that guides the user across the diorama.

```
                         +-----------------------------+
                         |      STANDBY / SLEEP        |
                         |  - Cat-loaf tucked limbs    |
                         |  - Horizontal aperture slit |
                         |  - 0.5 Hz amber chest pulse |
                         +--------------+--------------+
                                        ▲
                 Idle Timeout > 15s     │   User Interaction / Hover
                                        │
                         +--------------v--------------+
                         |      CURIOUS DISCOVERY      |
                         |  - Head tilt 15°-20°        |
                         |  - Dilated wide golden iris |
                         |  - Stylus arm deployed      |
                         |  - Friendly rising chirp    |
                         +--------------+--------------+
                                        ▲
                 Hover Hotspot          │   Click Workbench / Run Telemetry
                                        │
                         +--------------v--------------+
                         |     ACTIVE CALIBRATION      |
                         |  - Low forward quad stance  |
                         |  - Focused cyan laser beam  |
                         |  - 2.0 Hz vacuum tube pulse |
                         |  - Rapid multi-tone chirp   |
                         +-----------------------------+
```

### 5.1 Rigging & Kinematics Specification
- **Mesh Complexity**: 18,200 triangles. Single draw call via unified PBR texture atlas (albedo, roughness, metallic, normal, emission).
- **Bone Hierarchy**:
  - `Root_Body`
    - `Spine_Thorax`
      - `Neck` → `Head_Dome` (2-DoF Pitch/Yaw) → `Iris_Aperture` (Scale-based iris morph)
      - `Vacuum_Tube_Core` (Internal emissive mesh)
      - `Arm_Base` → `Arm_Segment1` → `Arm_Segment2` → `Stylus_Tip` (3-axis inverse kinematics)
    - `Leg_Front_L` / `Leg_Front_R` (3-bone IK chain with foot contact IK)
    - `Leg_Rear_L` / `Leg_Rear_R` (3-bone IK chain with foot contact IK)
    - `Grounding_Tether` (Verlet physics cable spline tethered to platform port)

### 5.2 Tri-State Autonomous State Machine
1. **Active Calibration (Focused)**:
   - *Trigger*: User triggers prompt distillation slider, selects drone flight path, or runs latency profiler.
   - *Physical Expression*: Drops into a low 4-point stance; rear limbs braced; optical iris contracts into a tight pinhole aperture emitting a crisp cyan laser projection line across the active workbench; chest vacuum tube core pulses at 2.0 Hz.
   - *Audio*: Fast multi-tone frequency modulation sweep (synthesized via Web Audio API bandpass filter).
2. **Curious Discovery (Inquisitive)**:
   - *Trigger*: User hovers an interactive 3D model, coffee glass, or succulent.
   - *Physical Expression*: Head tilts 15°–20° to the side; optical iris dilates wide with an illuminated golden ring; micro-tool stylus arm unlatches and points forward attentively.
   - *Audio*: Soft two-tone rising chirp (440Hz → 880Hz sine glide).
3. **Standby / Rest (Idle)**:
   - *Trigger*: Inactivity for > 15 seconds or switching to Light Mode (Dawn).
   - *Physical Expression*: Limbs fold inward beneath the titanium dome chassis into a compact "cat-loaf" loafing posture; optical iris closes to a fine horizontal amber slit; chest vacuum tube filament dims to a slow 0.5 Hz breathing cycle.
   - *Audio*: Low mechanical relaxation click and gentle 40Hz transformer hum.

### 5.3 Interactive Companion Dialogue System
- Clicking KURA-MK1 opens a speech bubble HUD rendered in retro monospaced typography with contextual tips:
  - *"Zone 1 active: Prompt optimization loop converged with +23.6% gain. Ready to inspect distillation tree?"*
  - *"Zone 2 active: Crazyflie trajectory controller listening on /cmd_vel at 100Hz."*
  - *"Tip: Press 'C' or click the phin filter to brew a fresh drop of cà phê sữa đá."*

---

## 6. Sensory Immersion, Easter Eggs & Da Nang Cultural Identity

### 6.1 Interactive Phin Coffee Simulation
- **Object**: Stainless steel Vietnamese coffee phin resting on a glass of rich condensed milk.
- **Interactivity**: Clicking the phin triggers a physics-driven drop of dark espresso falling through the clear glass, creating a ripple in the creamy condensed milk base.
- **Audio**: Ultra-crisp audio sample of a liquid droplet hitting milk (`phin_drop.mp3`), accompanied by a persistent on-screen counter: `Cà phê sữa đá: [N] drops brewed After Hours`.

### 6.2 Spatial Web Audio Architecture
The audio engine is built directly on the browser's native **Web Audio API** with a dedicated master gain bus, ensuring zero autoplay policy violations (initialized on first user click).

```
[Audio Context]
      │
      ├── Ambient Rain Sub-Bus ──── [Stereo Panner] ──── [Gain: 0.25] ──┐
      │   (Da Nang bay night rain & Han river coastal mist)             │
      │                                                                 │
      ├── Mechanical Hum Sub-Bus ── [Lowpass Biquad] ─── [Gain: 0.15] ──┼──> [Master Gain] ──> [Destination]
      │   (Crazyflie brushless motor & transformer 40Hz)                │          │
      │                                                                 │     (Mute/Unmute)
      ├── KURA Synthesizer Bus ──── [3D PannerNode] ──── [Gain: 0.30] ──┤
      │   (Positional chirps & calibration frequencies)                 │
      │                                                                 │
      └── UI Click & Drip Bus ───── [Stereo Panner] ──── [Gain: 0.40] ──┘
          (Mechanical keyboard clicks & coffee drips)
```

- **Bottom HUD Controls**:
  - Master Mute / Unmute toggle (defaults to muted).
  - Ambient Rain volume slider.
  - Lo-Fi Drone Hum volume slider.

### 6.3 Secret Console Commands & Developer Terminal
Developers who open Chrome DevTools (`F12` / `Cmd+Option+I`) are greeted with an ASCII art banner and a live JavaScript console interface exposed via `window.kura` and `window.giao`:

```javascript
// Exposed Developer Console API
window.kura = {
  setState: (state) => "Switched KURA to: " + state, // 'calibrating' | 'curious' | 'standby'
  scan: (zoneId) => "Scanning Zone: " + zoneId,       // 'prompt' | 'robotics' | 'cv' | 'archive'
  chirp: () => "Playing synthesizer chirp",
  status: () => ({ battery: "98.4%", firmware: "v2.6.4", node: "ROS2_HUMBLE_KURA" })
};

window.giao = {
  danangWeather: async () => ({ city: "Da Nang", bayTemp: "24°C", humidity: "82%", wind: "3.2m/s ESE" }),
  thesis: () => "Skills Distillation: Claude Haiku -> Gemma 4-26B (+23.6% accuracy)",
  brewCoffee: () => "☕ 1 fresh drop of cà phê sữa đá added to condensed milk!"
};
```

### 6.4 The Dragon Bridge Weekend Show Easter Egg
- **Secret Trigger**: Clicking the head of the golden Dragon Bridge in the background panorama triggers the legendary Da Nang weekend tradition:
  - The bridge head illuminates with an intense orange flare.
  - Emits an animated flame particle burst into the night sky, followed 2 seconds later by a cooling water-mist particle plume.
  - KURA-MK1 stops, turns its head toward the bridge, and enters Curious mode with an excited double chirp.

---

## 7. Frontend & Graphics Technology Stack

```
+----------------------------------------------------------------------------------------------------+
|                                    TECHNOLOGY STACK ARCHITECTURE                                   |
+--------------------------+---------------------------+---------------------------------------------+
| Layer                    | Technology                | Version / Specific Package                  |
+--------------------------+---------------------------+---------------------------------------------+
| Application Framework    | Next.js (App Router)      | v15.1.x (React 19, Turbopack)               |
| 3D Scene Graph Engine    | React Three Fiber (R3F)   | @react-three/fiber v9.x / Three.js r172+    |
| 3D Utility Helpers       | Drei                      | @react-three/drei v10.x                     |
| Post-Processing Pipeline | R3F Postprocessing        | @react-three/postprocessing v3.x            |
| Physics Engine           | Rapier 3D                 | @react-three/rapier v1.x                    |
| Camera & UI Animation    | GSAP & Framer Motion      | gsap v3.12.x / framer-motion v12.x          |
| Global State Management  | Zustand                   | zustand v5.x                                |
| 2D HUD & Styling         | Tailwind CSS              | tailwindcss v4.x + Lucide React             |
| Audio Engine             | Web Audio API             | Native Web Audio Graph                      |
+--------------------------+---------------------------+---------------------------------------------+
```

### 7.1 Component Architecture & Scene Graph Tree

```
<AppLayout>
  ├── <NavigationHUD />                   {/* 2D Header: Zone Jump, Theme Toggle, Audio Controls */}
  ├── <Canvas dpr={[1, 2]} gl={{ powerPreference: 'high-performance', antialias: false }}>
  │     ├── <PerspectiveCamera makeDefault position={[3.2, 2.8, 3.2]} fov={38} />
  │     ├── <OrbitControls enablePan={false} maxPolarAngle={Math.PI / 2.2} minDistance={2.5} maxDistance={6.0} />
  │     ├── <EnvironmentLighting />       {/* Directional, Warm Spotlights, Ambient navy */}
  │     ├── <SkyDomePanorama />           {/* Da Nang Bay Midnight Gradient & Son Tra Silhouette */}
  │     ├── <DragonBridgeMesh />          {/* Golden animated LED emission + Water reflections */}
  │     ├── <HanRiverWaterPlane />        {/* Custom Gerstner wave & normal reflection shader */}
  │     ├── <CoastalMistParticles />      {/* 300 instanced GPU dust motes */}
  │     │
  │     └── <DioramaPlatformGroup>        {/* Master Walnut & Anodized Aluminum Island */}
  │           ├── <UndercarriageStructure />
  │           ├── <StudioNameplateText />
  │           │
  │           ├── <ZoneSkillsDistillation /> {/* Terminals, Prompt Tree, Haiku-Gemma Slider */}
  │           ├── <ZoneRoboticsSimulation /> {/* Crazyflie Drone, Gimbal, Trajectory Splines */}
  │           ├── <ZoneBabyCarePerception /> {/* Nursery Crib, MediaPipe 33-pt Mesh, HUD */}
  │           ├── <ZoneGiaoArchiveRoom />    {/* 1:20 Cutaway Room Box, Desk Lamp Switch */}
  │           │
  │           ├── <KuraCompanionRobot />     {/* Rigged Droid, State Machine, NavMesh Movement */}
  │           └── <PhinCoffeeStation />      {/* Glass, Phin Filter, Animated Drip Particle */}
  │     │
  │     └── <EffectComposer multisampling={0}>
  │           ├── <Bloom luminanceThreshold={0.85} intensity={0.4} mipmapBlur />
  │           ├── <Vignette eskil={false} offset={0.15} darkness={0.65} />
  │           └── <ToneMapping mode={THREE.ACESFilmicToneMapping} />
  │
  ├── <ActiveZoneOverlayDrawer />         {/* 2D Slide-out Panel with In-depth Project Data */}
  └── <AccessibilityHotspotNav />         {/* Hidden Screen-Reader Navigation & Focus Trap */}
</AppLayout>
```

### 7.2 Zustand Global State Specification (`useStore.ts`)
```typescript
interface MicrositeState {
  // Navigation & Camera Focus
  activeZone: 'overview' | 'skills_distillation' | 'robotics' | 'babycare' | 'archive';
  cameraTarget: [number, number, number];
  cameraPosition: [number, number, number];
  setActiveZone: (zone: MicrositeState['activeZone']) => void;

  // Environment & Theme
  timeOfDay: 'after_hours' | 'dawn';
  toggleTimeOfDay: () => void;

  // KURA-MK1 State
  kuraState: 'calibrating' | 'curious' | 'standby';
  setKuraState: (state: MicrositeState['kuraState']) => void;

  // Interactivity Flags
  deskLampOn: boolean;
  toggleDeskLamp: () => void;
  flightTrajectory: 'lemniscate' | 'helix' | 'hover';
  setFlightTrajectory: (traj: MicrositeState['flightTrajectory']) => void;
  babyPose: 'supine' | 'prone' | 'rollover';
  setBabyPose: (pose: MicrositeState['babyPose']) => void;
  haikuGemmaRatio: number; // 0.0 (Haiku) to 1.0 (Gemma)
  setHaikuGemmaRatio: (val: number) => void;
  coffeeDripCount: number;
  incrementCoffeeDrip: () => void;

  // Audio System
  audioMuted: boolean;
  rainVolume: number;
  droneHumVolume: number;
  toggleAudioMute: () => void;
}
```

---

## 8. Performance Budget, Asset Optimization & WebGL Degradation Ladder

### 8.1 Quantitative Asset Size & Payload Budgets
Strict constraints ensure the microsite achieves instantaneous loading times even on mobile 4G networks:

```
+----------------------------------------------------------------------------------------------------+
|                                    QUANTITATIVE PAYLOAD BUDGETS                                    |
+------------------------------------+------------------+------------------+-------------------------+
| Asset Category                     | Target Budget    | Compression Tech | Verification Method     |
+------------------------------------+------------------+------------------+-------------------------+
| Master Diorama Platform GLB        | <= 2.20 MB       | Draco + Meshopt  | gltf-transform inspect  |
| KURA-MK1 Rigged Companion GLB      | <= 0.65 MB       | Meshopt Quantized| gltf-transform inspect  |
| Zone Props & Drone GLB             | <= 0.65 MB       | Meshopt Quantized| gltf-transform inspect  |
| **Total 3D Geometry Payload**      | **<= 3.50 MB**   | Meshopt Buffer   | CI File Size Assert     |
+------------------------------------+------------------+------------------+-------------------------+
| PBR Textures (Albedo, Norm, Rough) | <= 1.20 MB       | KTX2 Basis (UASTC)| toktx / basisu CLI     |
| Web Audio Compressed Chunks (MP3)  | <= 0.40 MB       | 96 kbps Joint-MP3| ffmpeg audio audit      |
| Next.js App Shell + JS Chunks      | <= 0.25 MB (gzip)| Turbopack Split  | next-bundle-analyzer    |
| Font Subsets & CSS Assets          | <= 0.08 MB       | WOFF2 Subsetting | glyphhanger audit       |
+------------------------------------+------------------+------------------+-------------------------+
| **TOTAL INITIAL PAGE LOAD**        | **<= 4.43 MB**   | Gzip / Brotli    | Lighthouse CI Gate      |
+------------------------------------+------------------+------------------+-------------------------+
```

### 8.2 Asset Optimization Pipeline Script
When implementing in Phase 3, 3D assets will pass through an automated `gltf-transform` pipeline:
```bash
# 1. Optimize geometry: reorder vertex cache, quantize attributes, compress with meshopt
npx @gltf-transform/cli optimize scene_raw.glb scene_optimized.glb \
  --compress meshopt \
  --quantize-position 14 \
  --quantize-normal 10 \
  --quantize-texcoord 12 \
  --texture-compress ktx2

# 2. Inspect output metrics
npx @gltf-transform/cli inspect scene_optimized.glb
```

### 8.3 The 4-Tier Progressive WebGL Degradation Ladder
To accommodate every device from high-end gaming rigs to entry-level smartphones and accessibility clients, the engine dynamically selects one of four runtime profiles:

```
+----------------------------------------------------------------------------------------------------+
|                                  PROGRESSIVE DEGRADATION LADDER                                    |
+-------------+---------------------------+----------------------------------------------------------+
| Tier        | Device Hardware Target    | Active Features & Render Settings                        |
+-------------+---------------------------+----------------------------------------------------------+
| **Tier 1**  | Desktop GPU / Apple M1+   | Full PBR Materials, 2.0 DPR, Dynamic 1024 Soft Shadows,  |
| High-End    | iPhone 13+ / Snapdragon 8 | Selective Bloom, Ambient Coastal Particles, 60 FPS Locked|
+-------------+---------------------------+----------------------------------------------------------+
| **Tier 2**  | Mid-tier Mobile           | 1.0 DPR, Baked Ambient Occlusion, Disabled Shadows,      |
| Standard    | Snapdragon 7 / A12 Bionic | Reduced 100 Particles, Bloom Disabled, 60 FPS Locked     |
+-------------+---------------------------+----------------------------------------------------------+
| **Tier 3**  | Budget Mobile / Low Battery| Fixed 30 FPS Cap, Simple Unlit/Lambert Shaders,          |
| Power Saver | WebGL 1.0 Fallback        | Static Camera Orbit, Disabled Particle Systems           |
+-------------+---------------------------+----------------------------------------------------------+
| **Tier 4**  | No WebGL / Browser Error /| **Interactive 2.5D CSS Parallax Canvas**:                |
| Zero WebGL  | prefers-reduced-motion    | High-res WebP diorama layers (hero_living_diorama.webp)  |
| Fallback    | Screen Reader Clients     | DOM Hotspot Buttons, Full Keyboard & WCAG 2.1 AA Support |
+-------------+---------------------------+----------------------------------------------------------+
```

---

## 9. Infrastructure, Hosting & CI/CD Deployment Pipeline

### 9.1 Hosting Architecture (Vercel & Cloudflare Edge)
- **Primary Hosting**: Vercel Serverless Edge Platform.
  - Next.js 15 App Router static generation (`output: 'export'` or SSG with Edge middleware).
  - Edge routing for geo-based Da Nang weather API telemetry.
- **Edge CDN Caching**:
  - Cloudflare Edge Network sitting in front of Vercel.
  - Implements immutable long-term caching for static 3D binaries:
    ```http
    Cache-Control: public, max-age=31536000, immutable
    Content-Type: model/gltf-binary
    Content-Encoding: br
    ```

### 9.2 CI/CD Quality Gate Pipeline (`.github/workflows/microsite-ci.yml`)
When implemented, every pull request must pass automated quality gates:
1. **Asset Size Linter**: Fails if any `.glb` exceeds 3.5 MB or if total payload exceeds 4.5 MB.
2. **Meshopt & KTX2 Validation**: Ensures 100% of textures are compressed in KTX2 format.
3. **Lighthouse CI (Mobile & Desktop)**:
   - Performance: $\ge 90$
   - Accessibility: $\ge 95$
   - Best Practices: $\ge 95$
   - SEO: $\ge 95$
4. **Playwright WebGL Visual Regression**: Takes automated snapshots of all four camera zone transitions, asserting pixel difference $< 1.5\%$.

---

## 10. Phase 3 Implementation Roadmap & Milestones

Following the completion of Phase 2B (README launch), the Level 2 microsite can be implemented seamlessly in 4 dedicated sprints:

```
+----------------------------------------------------------------------------------------------------+
|                                    PHASE 3 IMPLEMENTATION ROADMAP                                  |
+-----------+----------------------+-----------------------------------------------------------------+
| Sprint    | Name                 | Core Deliverables                                               |
+-----------+----------------------+-----------------------------------------------------------------+
| Sprint 1  | 3D Modeling & Assets | Blender 3D diorama modeling, 4 zone props, KURA-MK1 rigging,    |
|           | Pipeline             | gltf-transform Meshopt/KTX2 automated optimization pipeline     |
+-----------+----------------------+-----------------------------------------------------------------+
| Sprint 2  | R3F Scene Assembly   | Next.js 15 + R3F setup, environment lighting, Han River shader, |
|           | & Environment        | Dragon Bridge animation, camera orbital transitions             |
+-----------+----------------------+-----------------------------------------------------------------+
| Sprint 3  | Zone Interactivity   | Interactive prompt tree slider, Crazyflie trajectory controller,|
|           | & KURA Guide         | MediaPipe 33-pt mesh morphing, KURA tri-state state machine     |
+-----------+----------------------+-----------------------------------------------------------------+
| Sprint 4  | Polish, Audio & Edge | Web Audio API soundscape, phin drip simulation, console APIs,   |
|           | Deployment           | Tier 4 2.5D CSS fallback, Vercel/Cloudflare edge launch         |
+-----------+----------------------+-----------------------------------------------------------------+
```

---

## 11. Conclusion & Authorization

This architectural proposal blueprint provides the definitive, production-ready technical design for Level 2 (`docs/LEVEL_2_MICROSITE_PROPOSAL.md`). It establishes unambiguous scope boundaries, grounds every visual element in authentic robotics and computer science research, celebrates Toàn's hometown of Da Nang, and provides a bulletproof engineering roadmap for Phase 3.

**Recommendation:** Approve this architectural blueprint for inclusion in `docs/LEVEL_2_MICROSITE_PROPOSAL.md` upon completion of Milestone 2, while maintaining zero code additions to Phase 2B.
