<img src="assets/studio.png" alt="An imagined cutaway of Giáo’s studio: a computer vision desk, a robotics shelf, and a wall of research notes in teal, cream, and warm orange." width="100%">

# Come in. There’s something on the workbench.

I'm **Phan Văn Toàn** — **Giáo** to friends, `givoxxs` here.

I work across **robotics, AI, and software systems**: from body keypoints and small-model experiments to simulation and the backend that connects things.

This is my little studio on GitHub. Pick a project, open a notebook, follow a thread.

[The workbench](#the-workbench) · [The research notebook](#the-research-notebook) · [The tool shelf](#the-tool-shelf) · [Leave a note](mailto:phanvantoan.contact@gmail.com)

## The workbench

*A few things I've built. Open a drawer to look inside.*

<details open>
<summary><strong>The vision desk — Baby Posture Analysis</strong></summary>

### From pixels to posture.

A computer vision project for analyzing infant posture in images and video. It connects image preprocessing, MediaPipe body keypoints, and a Random Forest classifier to a FastAPI service.

```text
image / video → preprocessing → body keypoints → posture analysis → API
```

**Inside the drawer:** training notebooks, image and video analysis endpoints, a web interface, and Firebase integration.

**Made with:** Python · FastAPI · MediaPipe · OpenCV · scikit-learn

[Explore the project](https://github.com/givoxxs/baby_posture_analysis) · [Open the training notebooks](https://github.com/givoxxs/baby_posture_analysis/tree/main/ML_train)

</details>

<details>
<summary><strong>The experiment monitor — Skills Distillation</strong> · my 2026 thesis</summary>

### Can better instructions help a smaller model?

My graduation project explores rewriting structured skill documents through a **Student → Judge → Teacher** loop. The instructions change; the model weights do not.

The repository includes experiments on three skills, round-by-round results, and a dashboard for inspecting learning curves and instruction changes.

**Made with:** Python · LLM evaluation · FastAPI · Next.js

[Read the experiments](https://github.com/givoxxs/Skills_Distillation) · [Visit the dashboard](https://skills-distillation.vercel.app)

</details>

<details>
<summary><strong>The paper tray — VPP Document Agent</strong> · DevDay 2026 team project</summary>

### Making sense of a stack of scanned documents.

A team project for processing Japanese solar-project completion documents. My part focused on **PDF and image processing**, including extraction benchmarks and Vision LLM experiments.

**Made with:** Python · PyMuPDF · pdfplumber · Vision LLMs

[Meet the team & see my role](https://github.com/givoxxs/devday_2026_vibeteam#team--vibe-team) · [Read my research notes](https://github.com/givoxxs/devday_2026_vibeteam/blob/main/docs/research_toan.md)

</details>

<details>
<summary><strong>The city map — Da Nang Culinary Atlas</strong></summary>

### A backend for exploring food in the city.

A culinary discovery system with restaurants, dishes, reviews, geographic data, and role-based access. The backend brings these pieces together with Spring Boot and PostgreSQL.

**Made with:** Java · Spring Boot · PostgreSQL

[Explore the backend](https://github.com/givoxxs/Danang-Culinary-Atlas) · [See the frontend](https://github.com/givoxxs/Danang-Culinary-Atlas-FE)

</details>

## The research notebook

*One observation worth keeping next to the code.*

<details>
<summary><strong>The best round wasn't the last round.</strong> A note from Skills Distillation.</summary>

In the repository's reported experiments, all three skills peaked before their final round.

For `slack-gif-creator`, the score moved from **0.716** in round 1 to **0.886** at its peak, then finished at **0.865**. The reported **23.6% relative gain** compares round 1 with that peak, under this project's evaluation setup.

That leaves a useful question: when should an instruction-rewriting loop stop?

[See the results, methodology, and limitations](https://github.com/givoxxs/Skills_Distillation#kết-quả-thực-nghiệm)

</details>

## The tool shelf

**Robotics & edge** — ROS 2 · Isaac Sim · Gazebo · GAP SDK · PULP SDK<br>
**AI & vision** — PyTorch · TensorFlow · OpenCV · LLM evaluation<br>
**Software** — Python · C/C++ · TypeScript · Java · FastAPI · Spring Boot · PostgreSQL<br>
**Everyday tools** — Linux · Git · CI

<details>
<summary><strong>A little about the person at the desk</strong></summary>

My background is in Information Technology at **DUT, University of Danang**.

I'm interested in the space where models meet systems: simulation, edge intelligence, and useful software that makes experiments easier to run and understand.

[More repositories](https://github.com/givoxxs?tab=repositories) · [LinkedIn](https://www.linkedin.com/in/givoxxs/)

</details>

---

Have something interesting on your workbench? [Leave me a note.](mailto:phanvantoan.contact@gmail.com)
