function copyToClipboard(text) {
  navigator.clipboard.writeText(text).then(
    function () {
      console.log("Copied to clipboard successfully!");
    },
    function (err) {
      console.error("Could not copy text: ", err);
    }
  );
}

document.querySelectorAll(".copy-button").forEach((button) => {
  console.log("found button");
  button.addEventListener("click", function () {
    if (button.dataset.isCopying === "true") {
      return;
    }

    button.dataset.isCopying = "true";

    const link = button.dataset.text;
    copyToClipboard(link);

    button.classList.add("copied");
    const oldText = button.textContent;
    button.textContent = "Copied to clipboard 📋";

    setTimeout(() => {
      button.classList.remove("copied");
    }, 1000);

    setTimeout(() => {
      button.textContent = oldText;
      button.dataset.isCopying = "false";
    }, 2000);
  });
});
