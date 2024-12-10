const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

let audioContext = new AudioContext();
let analyser = audioContext.createAnalyser();
let source = null;

function startVisualization() {
  navigator.mediaDevices.getUserMedia({ audio: true })
    .then(stream => {
      source = audioContext.createMediaStreamSource(stream);
      source.connect(analyser);
      analyser.connect(audioContext.destination);

      const bufferLength = analyser.frequencyBinCount;
      const dataArray = new Uint8Array(bufferLength);

      function draw() {
        requestAnimationFrame(draw);
        analyser.getByteFrequencyData(dataArray);

        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = "hsl(0, 100%, 50%)";

        const barWidth = (canvas.width / bufferLength) * 2.5;
        for (let i = 0; i < bufferLength; i++) {
          const barHeight = dataArray[i];
          const x = i * barWidth;
          const y = canvas.height - barHeight;
          ctx.fillRect(x, y, barWidth, barHeight);
        }
      }

      draw();
    })
    .catch(err => {
      console.error("Error accessing microphone:", err);
    });
}

startVisualization();