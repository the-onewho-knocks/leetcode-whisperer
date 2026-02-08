const whisperBtn = document.getElementById("whisperBtn");
const problemInput = document.getElementById("problemInput");

const result = document.getElementById("result");
const patternEl = document.getElementById("pattern");
const analogyEl = document.getElementById("analogy");

const hintEls = {
  1: document.getElementById("hint1"),
  2: document.getElementById("hint2"),
  3: document.getElementById("hint3"),
};

whisperBtn.addEventListener("click", async () => {
  const problem = problemInput.value.trim();
  if (!problem) return;

  whisperBtn.innerText = "Whispering…";
  whisperBtn.disabled = true;

  const res = await fetch("http://127.0.0.1:8000/whisper/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      problem_statement: problem,
      user_code: "",
    }),
  });

  const data = await res.json();

  patternEl.innerText = data.pattern;
  analogyEl.innerText = data.chess_analogy;

  hintEls[1].innerText = data.hints.level_1;
  hintEls[2].innerText = data.hints.level_2;
  hintEls[3].innerText = data.hints.level_3;

  result.classList.remove("hidden");

  whisperBtn.innerText = "Whisper";
  whisperBtn.disabled = false;
});

document.querySelectorAll(".hint-btn").forEach((btn) => {
  btn.addEventListener("click", () => {
    const level = btn.dataset.level;
    const hint = hintEls[level];

    // 1. Make hint participate in layout
    hint.classList.remove("hidden");

    // 2. Trigger smooth animation
    requestAnimationFrame(() => {
      hint.classList.add("show");
    });

    // 3. Fade out button smoothly
    btn.style.opacity = "0";

    setTimeout(() => {
      btn.style.display = "none";
    }, 300);
  });
});