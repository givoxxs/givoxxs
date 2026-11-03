<p align="center">
  <img src="assets/banner_simulation_desk.png" alt="The Simulation Architect's Desk by the Bay" width="100%" style="border-radius: 8px;">
</p>

# Hi, I'm Phan Van Toan (Giáo)

<p>
  <strong>Software & Robotics Simulation Engineer · Creative Systems Tinkerer</strong><br>
  <em>Da Nang, Vietnam</em>
</p>

<p>
  <a href="#workbench">The Workbench</a> •
  <a href="#spatial-archive">The Spatial Archive</a> •
  <a href="#taxonomy">Technical Taxonomy</a> •
  <a href="#recognition">Recognition</a> •
  <a href="#connect">Connect</a>
</p>

---

### *"Before an autonomous system navigates the physical world, it must master thousands of flight hours in simulated physics."*

I am a software engineer specializing in **robotics simulation, digital twins, and autonomous systems**. I build high-fidelity virtual proving grounds, distributed middleware, and state estimation pipelines that allow autonomous machines (UAVs and mobile robots) to simulate, evaluate, and navigate with mathematical precision.

Beyond simulation engines, I love building creative software—ranging from interactive 3D WebGL spatial environments to automated model evaluation pipelines and full-stack digital platforms.

---

<h2 id="workbench">🛠️ The Workbench</h2>

*Selected projects exploring simulation, automated evaluation, computer vision, and systems engineering.*

<details open>
<summary><strong>🔬 Skills Distillation — Gradient-free Prompt Optimization (2026 Thesis)</strong></summary>
<br>

> *Can systematic instruction refactoring help a small language model match larger baselines without fine-tuning weights?*

An automated pipeline designed to distill complex agent skill specifications for Small Language Models (SLMs) without weight fine-tuning.

```text
Instruction Spec → Teacher Model → Student Execution (SLM) → Judge Evaluation Loop → Refined Prompt
```

- **Core Innovations:** Architected an automated **Teacher → Student → Judge** evaluation loop that systematically identifies failure modes and rewrites instruction schemas.
- **Empirical Results:** Achieved up to **+23.6% relative performance improvement** across benchmarked agent skills. Includes an interactive analytics dashboard for visualizing round-by-round convergence and instruction drift.
- **Tech Stack:** Python · Claude Haiku · OpenRouter (Gemma 4-26B) · FastAPI · Next.js

[Explore Repository ↗](https://github.com/givoxxs/Skills_Distillation) • [Live Dashboard ↗](https://skills-distillation.vercel.app)

</details>

<details>
<summary><strong>👁️ Baby Posture Analysis — BabyCare AI (Perception & Edge CV)</strong></summary>
<br>

> *Computer vision and lightweight intelligence for infant sleep safety.*

An IoT & computer vision perception system engineered to monitor infant sleep safety in real-time, detecting critical sleep postures (supine, prone, side) and blanket coverage to mitigate early risks.

- **Architecture:** Connected raw video streams through frame-level preprocessing, MediaPipe 33-point body landmark extraction, and lightweight classifiers (Random Forest, XGBoost) to achieve low-latency inference on edge nodes.
- **Integration:** Built the FastAPI streaming service with real-time push alerts to mobile applications.
- **Tech Stack:** Python · FastAPI · MediaPipe · OpenCV · Scikit-learn · XGBoost · Docker

[Explore Repository ↗](https://github.com/givoxxs/baby_posture_analysis)

</details>

<details>
<summary><strong>🗺️ Da Nang Culinary Atlas — Geospatial Mapping & Systems</strong></summary>
<br>

> *End-to-end data harvesting and spatial discovery platform for Da Nang food culture.*

A full-stack culinary mapping platform providing localized restaurant data, reviews, and route discovery across Da Nang.

- **Architecture:** Engineered automated distributed web-crawling pipelines with Playwright, custom schema normalization, and spatial PostgreSQL storage.
- **Delivery:** Built the administration dashboard in Next.js, real-time Mapbox navigation in React Native, and self-hosted CI/CD pipelines with automated SSL and reverse proxy routing.
- **Tech Stack:** Python (Playwright) · Next.js · React Native · Mapbox · PostgreSQL · Docker · Nginx

[Backend & Frontend Repo ↗](https://github.com/givoxxs/Danang-Culinary-Atlas) • [Crawler Pipeline ↗](https://github.com/givoxxs/Danang-Culinary-Atlas-FE)

</details>

<details>
<summary><strong>🎙️ Automated Video Summarization — Multimodal NLP</strong></summary>
<br>

> *Transforming long-form multimedia speech into structured, actionable intelligence.*

An automated speech-to-text and summarization pipeline for processing multimedia video recordings. Utilized OpenAI Whisper for acoustic transcription and Transformer-based NLP pipelines for segment extraction and concise summarization.

- **Tech Stack:** Python · OpenAI Whisper · HuggingFace Transformers · NLTK

[Explore Repository ↗](https://github.com/givoxxs)

</details>

---

<h2 id="spatial-archive">🏛️ The Spatial Archive</h2>

*When graduation came, I didn't want to send a PDF or an email invitation. I built an interactive 3D memory room instead.*

<p align="center">
  <a href="https://the-giao-archive.vercel.app/" target="_blank">
    <strong>👉 Step inside: The Giáo Archive (Interactive 3D WebGL Room) ↗</strong>
  </a>
</p>

An in-browser spatial experience built with **Three.js** and **WebGL**. Visitors can toggle room lighting, rotate and orbit the isometric camera, inspect items on the bookshelf, and unlock campus memories and projects preserved in a virtual room.

- **Stack:** Three.js · WebGL · React · Vite · Vercel

---

<h2 id="taxonomy">🧭 Technical Taxonomy</h2>

```text
┌───────────────────────────────┬───────────────────────────────┬───────────────────────────────┐
│     SIMULATION & ROBOTICS     │     PERCEPTION & AI LAB       │    SYSTEMS & CREATIVE WEB     │
├───────────────────────────────┼───────────────────────────────┼───────────────────────────────┤
│ • ROS 2 (Humble) & FastDDS    │ • PyTorch & Deep Learning     │ • Three.js & WebGL (3D Web)   │
│ • Gazebo & Isaac Sim          │ • OpenCV & MediaPipe          │ • Next.js & React Native      │
│ • PX4 Autopilot & UAV Sim     │ • Scikit-learn & XGBoost      │ • FastAPI & Node.js           │
│ • State Estimation (OpenVINS) │ • SLM / LLM Evaluation        │ • C / C++ & Python            │
│ • Telemetry & QEMU / VMs      │ • Automatic Prompt Opt. (APO) │ • Docker, Linux & CI/CD       │
│ • High-Fidelity Digital Twins │ • Computer Vision Pipelines   │ • PostgreSQL, MongoDB, Redis  │
└───────────────────────────────┴───────────────────────────────┴───────────────────────────────┘
```

---

<h2 id="recognition">🏆 Recognition & Background</h2>

- **Best Architecture Award** — *Real-World AI Implementation Competition (TAS Design Group / DEVDAY2026)*  
  Validated ability to design scalable, robust, and low-latency system architectures for complex AI-driven applications.
- **Most Favorite Team** — *UniHack 2024 (Digital Tourism)*  
  Developed a high-impact mobile application connecting freelance local guides with travelers.
- **Academic Foundation** — *Da Nang University of Science and Technology (DUT)*  
  Bachelor of Information Technology (Enterprise Cooperation Program) · **GPA: 3.54 / 4.0** (Expected Graduation: 2026).

---

<h2 id="connect">📬 Connect</h2>

I'm always keen to talk about physics simulation, autonomous flight stacks, digital twins, or creative 3D web engineering:

- **LinkedIn:** [linkedin.com/in/givoxxs](https://www.linkedin.com/in/givoxxs/)
- **GitHub:** [github.com/givoxxs](https://github.com/givoxxs)
- **Email:** [phanvantoan.contact@gmail.com](mailto:phanvantoan.contact@gmail.com)

<br>

<p align="center">
  <sub>Crafted with passion in Da Nang, Vietnam · 2026</sub>
</p>
