# VIAMI TEST — Interactive travel app prototype

**An independent mobile-first demo built for comparison with the existing VIAMI app.**

![VIAMI TEST interface previews](docs/preview-screens.png)

### Features in the demo

- Animated onboarding and local demo profile (not real login)
- Discover catalog, category filters, saved trips
- Create a trip and request to join a group
- In-browser group chat, voting and participation confirmation
- Interactive Portugal itinerary with visited stops and timestamps
- Flight date matching with trip duration constraints (**simulated prices, no live flight API**)
- Support inbox and illustrative admin dashboard (**not a secure admin tool**)
- Local browser persistence and responsive layout

### Run locally

```sh
python -m http.server 8765
```

Open `http://localhost:8765`.

### Publish the mobile demo via GitHub Pages

1. Create a new public GitHub repository named `viamitest`.
2. Push these files to the repository's `main` branch.
3. Go to **Settings → Pages → Build and deployment → Source: GitHub Actions**.
4. Wait until **Actions → Publish VIAMI TEST to GitHub Pages** is successful.
5. Visit `https://<your-login>.github.io/viamitest/` on a phone.

A ready-made deployment workflow lives in `.github/workflows/pages.yml`. For complete Russian setup instructions, see [GITHUB_START_HERE.md](GITHUB_START_HERE.md).

> **Disclaimer:** This is a standalone local prototype, not a copy of the original app. It has no real user authentication, server sync, identity verification, payment processing or privileged/admin access control. Do not upload actual ID documents, passwords or payment data. All interactive demo content is stored on your current device in browser storage.