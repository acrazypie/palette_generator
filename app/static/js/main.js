const API_URL = "/api/generate";

class ThemeManager {
    constructor() {
        this.theme = localStorage.getItem("theme") || "dark";
        this.init();
    }

    init() {
        this.applyTheme(this.theme);
        this.setupThemeToggle();
    }

    setupThemeToggle() {
        const themeToggles = document.querySelectorAll(".theme-toggle");
        themeToggles.forEach((toggle) => {
            toggle.addEventListener("click", (e) => {
                const selectedTheme = e.currentTarget.dataset.theme;
                this.setTheme(selectedTheme);
            });
        });
    }

    setTheme(theme) {
        this.theme = theme;
        this.applyTheme(theme);
        localStorage.setItem("theme", theme);
    }

    applyTheme(theme) {
        const body = document.body;
        if (theme === "light") {
            body.classList.add("light-theme");
        } else {
            body.classList.remove("light-theme");
        }
        this.updateThemeToggleButtons();
    }

    updateThemeToggleButtons() {
        const themeToggles = document.querySelectorAll(".theme-toggle");
        themeToggles.forEach((toggle) => {
            toggle.classList.remove("selected");
            if (
                (this.theme === "dark" && toggle.dataset.theme === "dark") ||
                (this.theme === "light" && toggle.dataset.theme === "light")
            ) {
                toggle.classList.add("selected");
            }
        });
    }
}

class PaletteGenerator {
    constructor() {
        this.baseColorElement = document.getElementById("baseColor");
        this.modeSelectElement = document.getElementById("modeSelect");
        this.countInputElement = document.getElementById("countInput");
        this.generateBtn = document.getElementById("generatebtn");
        this.paletteContainer = document.getElementById("palette");
        this.baseColor = this.baseColorElement.value;
        this.mode = this.modeSelectElement.value;
        this.count = parseInt(this.countInputElement.value);
        this.init();
    }

    init() {
        console.log("Palette Generator Loaded");
        this.setupEventListeners();
    }

    setupEventListeners() {
        this.baseColorElement.addEventListener("input", (e) => {
            this.baseColor = e.target.value;
        });

        this.modeSelectElement.addEventListener("change", (e) => {
            this.mode = e.target.value;
        });

        this.countInputElement.addEventListener("change", (e) => {
            this.count = parseInt(e.target.value);
        });

        this.generateBtn.addEventListener("click", () =>
            this.generatePalette()
        );

        // Generate palette on page load
        this.generatePalette();
    }

    async generatePalette() {
        try {
            const response = await fetch(API_URL, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    base_color: this.baseColor,
                    mode: this.mode,
                    count: this.count,
                }),
            });

            const data = await response.json();

            if (!data.success) {
                console.error("Error:", data.error);
                this.showError(data.error);
                return;
            }

            this.renderPalette(data.palette);
        } catch (error) {
            console.error("Fetch error:", error);
            this.showError("Failed to generate palette");
        }
    }

    renderPalette(colors) {
        this.paletteContainer.innerHTML = "";

        colors.forEach((color) => {
            const colorBox = document.createElement("div");
            colorBox.classList.add("color-box");
            colorBox.style.background = color;
            colorBox.style.color = this.getTextColor(color);
            colorBox.textContent = color;
            colorBox.title = `Click to copy: ${color}`;

            // Copy to clipboard on click
            colorBox.addEventListener("click", () => {
                navigator.clipboard.writeText(color);
                this.showNotification(`Copied: ${color}`);
            });

            this.paletteContainer.appendChild(colorBox);
        });
    }

    getTextColor(hexColor) {
        const rgb = parseInt(hexColor.slice(1), 16);
        const r = (rgb >> 16) & 255;
        const g = (rgb >> 8) & 255;
        const b = rgb & 255;
        const brightness = (r * 299 + g * 587 + b * 114) / 1000;
        return brightness > 155 ? "#000000" : "#FFFFFF";
    }

    showError(message) {
        const errorDiv = document.createElement("div");
        errorDiv.style.color = "red";
        errorDiv.style.padding = "10px";
        errorDiv.style.marginTop = "10px";
        errorDiv.textContent = `Error: ${message}`;
        this.paletteContainer.innerHTML = "";
        this.paletteContainer.appendChild(errorDiv);
    }

    showNotification(message) {
        const notification = document.createElement("div");
        notification.style.position = "fixed";
        notification.style.top = "10px";
        notification.style.right = "10px";
        notification.style.background = "#4CAF50";
        notification.style.color = "white";
        notification.style.padding = "12px 20px";
        notification.style.borderRadius = "4px";
        notification.style.zIndex = "1000";
        notification.textContent = message;
        document.body.appendChild(notification);

        setTimeout(() => {
            notification.remove();
        }, 2000);
    }
}

document.addEventListener("DOMContentLoaded", () => {
    new ThemeManager();
    new PaletteGenerator();
});
