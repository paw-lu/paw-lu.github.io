/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./theme/**/*.html", "./theme/**/*.js"],
  theme: {
    colors: {
      primary: "#496727",
      secondary: "#59614e",
      background: "#fefcf6",
      "on-background": "#1b1c18",
      "on-primary-container": "#0f2000",
      "secondary-container": "#dde6cd",
      "on-secondary-container": "#171e0e",
      "surface-variant": "#e2e4d8",
      "on-surface-variant": "#45483f",
    },
    extend: {
      typography: ({ theme }) => ({
        "on-background": {
          css: {
            "--tw-prose-body": theme("colors.on-background"),
            "--tw-prose-headings": theme("colors.on-background"),
            "--tw-prose-lead": theme("colors.on-background"),
            "--tw-prose-links": theme("colors.primary"),
            "--tw-prose-bold": theme("colors.on-background"),
            "--tw-prose-counters": theme("colors.on-background"),
            "--tw-prose-bullets": theme("colors.on-background"),
            "--tw-prose-hr": theme("colors.on-background"),
            "--tw-prose-quotes": theme("colors.on-background"),
            "--tw-prose-quote-borders": theme("colors.on-background"),
            "--tw-prose-captions": theme("colors.on-background"),
            "--tw-prose-code": theme("colors.on-surface-variant"),
            "--tw-prose-code-bg": theme("colors.surface-variant"),
            "--tw-prose-pre-code": theme("colors.on-surface-variant"), // TODO: Probably get rid of this late
            "--tw-prose-pre-bg": theme("colors.surface-variant"),
            "--tw-prose-th-borders": theme("colors.on-background"),
            "--tw-prose-td-borders": theme("colors.on-background"),
            "--tw-prose-invert-body": theme("colors.on-background"),
            "--tw-prose-invert-headings": theme("colors.on-background"),
            "--tw-prose-invert-lead": theme("colors.on-background"),
            "--tw-prose-invert-links": theme("colors.primary"),
            "--tw-prose-invert-bold": theme("colors.on-background"),
            "--tw-prose-invert-counters": theme("colors.on-background"),
            "--tw-prose-invert-bullets": theme("colors.on-background"),
            "--tw-prose-invert-hr": theme("colors.on-background"),
            "--tw-prose-invert-quotes": theme("colors.on-background"),
            "--tw-prose-invert-quote-borders": theme("colors.on-background"),
            "--tw-prose-invert-captions": theme("colors.on-background"),
            "--tw-prose-invert-code": theme("colors.on-surface-variant"),
            "--tw-prose-invert-code-bg": theme("colors.surface-variant"),
            "--tw-prose-invert-pre-code": theme("colors.on-background"),
            "--tw-prose-invert-pre-bg": theme("colors.surface-variant"),
            "--tw-prose-invert-th-borders": theme("colors.on-background"),
            "--tw-prose-invert-td-borders": theme("colors.on-background"),
          },
        },
      }),
      fontSize: {
        "display-large": [
          "3.5625rem",
          { lineHeight: "4rem", letterSpacing: "0em", fontWeight: "400" },
        ],
        "headline-large": [
          "2rem",
          { lineHeight: "2.5rem", letterSpacing: "0em", fontWeight: "400" },
        ],
        "headline-medium": [
          "1.75rem",
          { lineHeight: "2.25rem", letterSpacing: "0em", fontWeight: "400" },
        ],
        "headline-small": [
          "1.5rem",
          { lineHeight: "2.25rem", letterSpacing: "0em", fontWeight: "400" },
        ],
        "title-medium": [
          "1rem",
          {
            lineHeight: "1.5rem",
            letterSpacing: "0.009375em",
            fontWeight: "700",
          },
        ],
        "body-large": [
          "1rem",
          {
            lineHeight: "1.5rem",
            letterSpacing: "0.03125em",
            fontWeight: "400",
          },
        ],
        "label-large": [
          "0.875rem",
          {
            lineHeight: "1.25rem",
            letterSpacing: "0.00625",
            fontWeight: "500",
          },
        ],
      },
    },
    fontFamily: {
      body: ["Space Grotesk"],
      display: ["Space Mono"],
      code: ["Fragment Mono"],
    },
  },
  plugins: [require("@tailwindcss/typography")],
};
