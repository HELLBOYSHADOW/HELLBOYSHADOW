import os

with open('images/ghost_b64.txt', 'r') as f:
    b64_data = f.read().strip()

svg_template = f'''<svg xmlns="http://www.w3.org/2000/svg"
     xmlns:xlink="http://www.w3.org/1999/xlink"
     viewBox="0 0 1200 600"
     width="100%"
     height="100%"
     style="max-width: 100%; height: auto; display: block; background: #010803;"
     preserveAspectRatio="xMidYMid meet">

  <defs>
    <!-- Background Gradient -->
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#020804"/>
      <stop offset="50%" stop-color="#051409"/>
      <stop offset="100%" stop-color="#010402"/>
    </linearGradient>

    <!-- Neon Text Gradient -->
    <linearGradient id="neon" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="30%" stop-color="#73ff9c"/>
      <stop offset="70%" stop-color="#00ff41"/>
      <stop offset="100%" stop-color="#009926"/>
    </linearGradient>

    <!-- Header Accent Gradient -->
    <linearGradient id="headerGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#00ff41" stop-opacity="0.8"/>
      <stop offset="60%" stop-color="#00ff41" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#00ff41" stop-opacity="0"/>
    </linearGradient>

    <!-- Digital Rain Gradient -->
    <linearGradient id="rain" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0"/>
      <stop offset="40%" stop-color="#00ff41" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#003b0f" stop-opacity="0.05"/>
    </linearGradient>

    <!-- Glow Filters -->
    <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="3.5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <filter id="softGlow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="14"/>
    </filter>

    <!-- Cyber Rim Glow for Operative -->
    <filter id="cyberGlow" x="-30%" y="-30%" width="160%" height="160%">
      <feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="#00ff41" flood-opacity="0.6"/>
      <feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="#00ff41" flood-opacity="0.25"/>
    </filter>

    <!-- Background Grid Pattern -->
    <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse">
      <path d="M 32 0 L 0 0 0 32" fill="none" stroke="#00ff41" stroke-opacity="0.07" stroke-width="0.75"/>
    </pattern>

    <!-- Scanlines Pattern -->
    <pattern id="scanlines" width="4" height="4" patternUnits="userSpaceOnUse">
      <line x1="0" y1="0" x2="4" y2="0" stroke="#00ff41" stroke-width="1" stroke-opacity="0.04"/>
    </pattern>

    <!-- Smooth Vignette -->
    <radialGradient id="vignette" cx="50%" cy="50%" r="70%">
      <stop offset="0%" stop-color="#000000" stop-opacity="0"/>
      <stop offset="60%" stop-color="#000000" stop-opacity="0.15"/>
      <stop offset="85%" stop-color="#000000" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0.75"/>
    </radialGradient>

    <!-- Operative Bottom Feathering Mask -->
    <linearGradient id="ghostBottomFade" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="1"/>
      <stop offset="80%" stop-color="#ffffff" stop-opacity="1"/>
      <stop offset="93%" stop-color="#ffffff" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>
    </linearGradient>

    <mask id="ghostMask" maskUnits="userSpaceOnUse" x="650" y="0" width="550" height="600">
      <rect x="650" y="0" width="550" height="600" fill="url(#ghostBottomFade)"/>
    </mask>

    <!-- Banner boundaries -->
    <clipPath id="bannerClip">
      <rect width="1200" height="600" rx="8"/>
    </clipPath>
  </defs>

  <g clip-path="url(#bannerClip)">

    <!-- ================================== -->
    <!-- BASE LAYERS                        -->
    <!-- ================================== -->
    <rect width="1200" height="600" fill="url(#bg)"/>
    <rect width="1200" height="600" fill="url(#grid)"/>

    <!-- Ambient green illumination behind operative & HUD -->
    <ellipse cx="940" cy="290" rx="260" ry="240" fill="#00ff41" opacity="0.10" filter="url(#softGlow)"/>
    <ellipse cx="360" cy="280" rx="280" ry="220" fill="#00ff41" opacity="0.04" filter="url(#softGlow)"/>

    <!-- ================================== -->
    <!-- MATRIX DIGITAL RAIN (BACKGROUND)   -->
    <!-- ================================== -->
    <g fill="#00ff41" font-family="'Consolas', 'Courier New', monospace" font-size="14" opacity="0.45">
      <!-- Rain column 1 -->
      <text x="25" y="0">
        <tspan x="25" dy="18">0</tspan><tspan x="25" dy="18">1</tspan><tspan x="25" dy="18">1</tspan>
        <tspan x="25" dy="18">0</tspan><tspan x="25" dy="18">1</tspan><tspan x="25" dy="18">0</tspan>
        <tspan x="25" dy="18">1</tspan><tspan x="25" dy="18">1</tspan>
        <animateTransform attributeName="transform" type="translate" values="0 -140; 0 520" dur="8s" repeatCount="indefinite"/>
      </text>

      <!-- Rain column 2 -->
      <text x="680" y="0">
        <tspan x="680" dy="18">1</tspan><tspan x="680" dy="18">0</tspan><tspan x="680" dy="18">0</tspan>
        <tspan x="680" dy="18">1</tspan><tspan x="680" dy="18">1</tspan><tspan x="680" dy="18">0</tspan>
        <tspan x="680" dy="18">1</tspan><tspan x="680" dy="18">0</tspan>
        <animateTransform attributeName="transform" type="translate" values="0 -100; 0 550" dur="9.5s" repeatCount="indefinite"/>
      </text>

      <!-- Rain column 3 (Behind Operative) -->
      <text x="735" y="0" opacity="0.3">
        <tspan x="735" dy="18">0</tspan><tspan x="735" dy="18">1</tspan><tspan x="735" dy="18">0</tspan>
        <tspan x="735" dy="18">1</tspan><tspan x="735" dy="18">1</tspan><tspan x="735" dy="18">0</tspan>
        <animateTransform attributeName="transform" type="translate" values="0 -120; 0 500" dur="11s" repeatCount="indefinite"/>
      </text>

      <!-- Rain column 4 (Far Right) -->
      <text x="1145" y="0">
        <tspan x="1145" dy="18">1</tspan><tspan x="1145" dy="18">1</tspan><tspan x="1145" dy="18">0</tspan>
        <tspan x="1145" dy="18">1</tspan><tspan x="1145" dy="18">0</tspan><tspan x="1145" dy="18">1</tspan>
        <tspan x="1145" dy="18">0</tspan><tspan x="1145" dy="18">0</tspan>
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 600" dur="7.5s" repeatCount="indefinite"/>
      </text>
    </g>

    <!-- Code rain vertical trails -->
    <g stroke="url(#rain)" stroke-width="1.8" opacity="0.4">
      <line x1="45" y1="-50" x2="45" y2="150">
        <animate attributeName="y1" values="-100;450;-100" dur="6.5s" repeatCount="indefinite"/>
        <animate attributeName="y2" values="100;650;100" dur="6.5s" repeatCount="indefinite"/>
      </line>
      <line x1="695" y1="-80" x2="695" y2="140">
        <animate attributeName="y1" values="-80;480;-80" dur="8s" repeatCount="indefinite"/>
        <animate attributeName="y2" values="140;700;140" dur="8s" repeatCount="indefinite"/>
      </line>
      <line x1="1165" y1="-100" x2="1165" y2="120">
        <animate attributeName="y1" values="-100;500;-100" dur="7s" repeatCount="indefinite"/>
        <animate attributeName="y2" values="120;720;120" dur="7s" repeatCount="indefinite"/>
      </line>
    </g>

    <!-- ================================== -->
    <!-- TOP STATUS BAR / HEADER            -->
    <!-- ================================== -->
    <g font-family="'Consolas', 'Courier New', monospace" font-size="11" fill="#00ff41">
      <!-- Top header line -->
      <path d="M 30 46 L 660 46" stroke="url(#headerGrad)" stroke-width="1.5"/>
      <path d="M 720 46 L 1170 46" stroke="url(#headerGrad)" stroke-width="1.5"/>

      <!-- Pulse indicator -->
      <circle cx="40" cy="30" r="4" fill="#00ff41" filter="url(#glow)">
        <animate attributeName="opacity" values="1;0.2;1" dur="1.8s" repeatCount="indefinite"/>
      </circle>
      <text x="52" y="34" letter-spacing="1.5" opacity="0.95">SYSTEM: ONLINE</text>
      <text x="195" y="34" opacity="0.5">|</text>
      <text x="215" y="34" letter-spacing="1.2" opacity="0.8">KERNEL: MATRIX-CORE // v4.4.4</text>
      <text x="460" y="34" opacity="0.5">|</text>
      <text x="480" y="34" letter-spacing="1.2" fill="#6aff8a" opacity="0.85">CLEARANCE: LVL_5 [ROOT]</text>

      <text x="1160" y="34" text-anchor="end" letter-spacing="1.5" opacity="0.85">NET: ENCRYPTED [444-NODE]</text>
    </g>

    <!-- ================================== -->
    <!-- LEFT PANEL: HUD / TERMINAL CONSOLE -->
    <!-- ================================== -->
    <!-- Terminal Panel Frame -->
    <g fill="none" stroke="#00ff41">
      <!-- Main Left Container -->
      <rect x="35" y="60" width="635" height="495" rx="4"
            fill="#031206" fill-opacity="0.35"
            stroke="#00ff41" stroke-opacity="0.25" stroke-width="1"/>

      <!-- Tech corners on left container -->
      <path d="M 35 80 L 35 60 L 55 60" stroke="#00ff41" stroke-width="2" filter="url(#glow)"/>
      <path d="M 650 60 L 670 60 L 670 80" stroke="#00ff41" stroke-width="2" filter="url(#glow)"/>
      <path d="M 35 535 L 35 555 L 55 555" stroke="#00ff41" stroke-width="2" filter="url(#glow)"/>
      <path d="M 650 555 L 670 555 L 670 535" stroke="#00ff41" stroke-width="2" filter="url(#glow)"/>
    </g>

    <!-- Terminal Header Prompt -->
    <g font-family="'Consolas', 'Courier New', monospace" font-size="11" fill="#00ff41">
      <rect x="52" y="75" width="225" height="22" rx="3" fill="#00ff41" fill-opacity="0.12"/>
      <text x="60" y="90" letter-spacing="1.2" fill="#7dff9e" font-weight="bold">
        root@matrix:~$ ./identify
      </text>

      <text x="645" y="90" text-anchor="end" letter-spacing="1" opacity="0.6">
        ID: 0x7F-SHADOW
      </text>
    </g>

    <!-- Hero Title: SREERAG R -->
    <!-- Name Glow Underlayer -->
    <text x="52" y="152"
          font-family="'Arial Black', 'Impact', sans-serif"
          font-size="52"
          font-weight="900"
          letter-spacing="3"
          fill="#00ff41"
          opacity="0.5"
          filter="url(#softGlow)">
      SREERAG R
    </text>

    <!-- Name Main Text -->
    <text x="52" y="152"
          font-family="'Arial Black', 'Impact', sans-serif"
          font-size="52"
          font-weight="900"
          letter-spacing="3"
          fill="url(#neon)"
          stroke="#00ff41"
          stroke-width="0.8"
          filter="url(#glow)">
      SREERAG R
    </text>

    <!-- Subtitle / Title Bar -->
    <g font-family="'Consolas', 'Courier New', monospace">
      <text x="54" y="184"
            font-size="14.5"
            font-weight="bold"
            letter-spacing="2"
            fill="#baffc9">
        SOFTWARE ENGINEER  •  APPLIED AI ARCHITECT
      </text>

      <!-- Decorative Divider with Tick Marks -->
      <line x1="52" y1="198" x2="650" y2="198" stroke="#00ff41" stroke-width="1.5" stroke-opacity="0.7" filter="url(#glow)"/>
      <line x1="52" y1="202" x2="280" y2="202" stroke="#00ff41" stroke-width="0.8" stroke-opacity="0.4"/>
      <rect x="52" y="196" width="6" height="5" fill="#00ff41"/>
      <rect x="644" y="196" width="6" height="5" fill="#00ff41"/>
    </g>

    <!-- ================================== -->
    <!-- MODULAR TELEMETRY CARDS (2x2 GRID) -->
    <!-- ================================== -->

    <!-- Card 1: CORE / ROLE -->
    <g transform="translate(52, 218)">
      <rect width="288" height="68" rx="3" fill="#021406" fill-opacity="0.6" stroke="#00ff41" stroke-opacity="0.3" stroke-width="1"/>
      <path d="M 0 12 L 0 0 L 12 0" stroke="#00ff41" stroke-width="1.5" fill="none"/>
      <text x="12" y="22" font-family="'Consolas', monospace" font-size="10" fill="#00ff41" letter-spacing="1.5" opacity="0.8">
        [>] DIRECTIVE // 01
      </text>
      <text x="12" y="40" font-family="'Consolas', monospace" font-size="13" font-weight="bold" fill="#ffffff" letter-spacing="1">
        FULL STACK &amp; AI AGENTS
      </text>
      <text x="12" y="56" font-family="'Consolas', monospace" font-size="10" fill="#6aff8a" letter-spacing="1">
        Building Autonomous Workflows
      </text>
    </g>

    <!-- Card 2: TECH STACK -->
    <g transform="translate(352, 218)">
      <rect width="298" height="68" rx="3" fill="#021406" fill-opacity="0.6" stroke="#00ff41" stroke-opacity="0.3" stroke-width="1"/>
      <path d="M 0 12 L 0 0 L 12 0" stroke="#00ff41" stroke-width="1.5" fill="none"/>
      <text x="12" y="22" font-family="'Consolas', monospace" font-size="10" fill="#00ff41" letter-spacing="1.5" opacity="0.8">
        [>] TECH ARSENAL // 02
      </text>
      <text x="12" y="40" font-family="'Consolas', monospace" font-size="13" font-weight="bold" fill="#ffffff" letter-spacing="1">
        PYTHON • TS • NEXT.JS
      </text>
      <text x="12" y="56" font-family="'Consolas', monospace" font-size="10" fill="#6aff8a" letter-spacing="1">
        PyTorch • FastEngine • Docker
      </text>
    </g>

    <!-- Card 3: STATUS / UPTIME -->
    <g transform="translate(52, 298)">
      <rect width="288" height="68" rx="3" fill="#021406" fill-opacity="0.6" stroke="#00ff41" stroke-opacity="0.3" stroke-width="1"/>
      <path d="M 0 12 L 0 0 L 12 0" stroke="#00ff41" stroke-width="1.5" fill="none"/>
      <text x="12" y="22" font-family="'Consolas', monospace" font-size="10" fill="#00ff41" letter-spacing="1.5" opacity="0.8">
        [>] SYSTEM STATUS // 03
      </text>
      <circle cx="18" cy="38" r="4.5" fill="#00ff41" filter="url(#glow)">
        <animate attributeName="opacity" values="1;0.3;1" dur="1.2s" repeatCount="indefinite"/>
      </circle>
      <text x="30" y="42" font-family="'Consolas', monospace" font-size="13" font-weight="bold" fill="#00ff41" letter-spacing="1">
        100% OPERATIONAL
      </text>
      <text x="12" y="58" font-family="'Consolas', monospace" font-size="10" fill="#6aff8a" letter-spacing="1">
        Latency: 1ms • Loss: 0.00%
      </text>
    </g>

    <!-- Card 4: PROTOCOL / MISSION -->
    <g transform="translate(352, 298)">
      <rect width="298" height="68" rx="3" fill="#021406" fill-opacity="0.6" stroke="#00ff41" stroke-opacity="0.3" stroke-width="1"/>
      <path d="M 0 12 L 0 0 L 12 0" stroke="#00ff41" stroke-width="1.5" fill="none"/>
      <text x="12" y="22" font-family="'Consolas', monospace" font-size="10" fill="#00ff41" letter-spacing="1.5" opacity="0.8">
        [>] CODEX PROTOCOL // 04
      </text>
      <text x="12" y="40" font-family="'Consolas', monospace" font-size="13" font-weight="bold" fill="#ffffff" letter-spacing="1">
        INNOVATE • SHIP • ITERATE
      </text>
      <text x="12" y="56" font-family="'Consolas', monospace" font-size="10" fill="#6aff8a" letter-spacing="1">
        Neural Architecture Evolution
      </text>
    </g>

    <!-- ================================== -->
    <!-- BOTTOM TELEMETRY / RADAR MODULE    -->
    <!-- ================================== -->

    <!-- Radar Compass (Bottom-Left) -->
    <g transform="translate(105, 455)" fill="none" stroke="#00ff41" opacity="0.75">
      <!-- Radar outer rings -->
      <circle r="60" stroke-width="1" stroke-dasharray="3 5"/>
      <circle r="45" stroke-width="1.2" stroke-dasharray="25 6 3 6">
        <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="20s" repeatCount="indefinite"/>
      </circle>
      <circle r="25" stroke-width="0.8" stroke-dasharray="4 4">
        <animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="12s" repeatCount="indefinite"/>
      </circle>
      <circle r="3" fill="#00ff41"/>
      <!-- Crosshairs -->
      <line x1="-66" y1="0" x2="66" y2="0" stroke-width="0.8" stroke-opacity="0.5"/>
      <line x1="0" y1="-66" x2="0" y2="66" stroke-width="0.8" stroke-opacity="0.5"/>
      <!-- Sweeping radar line -->
      <line x1="0" y1="0" x2="56" y2="-20" stroke="#00ff41" stroke-width="1.5" filter="url(#glow)">
        <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="4s" repeatCount="indefinite"/>
      </line>
    </g>

    <!-- Live System Terminal Stream (Bottom-Right of Left Panel) -->
    <g transform="translate(195, 395)" font-family="'Consolas', monospace" font-size="10" fill="#00ff41">
      <text y="15" letter-spacing="1" opacity="0.8">
        &gt; NEURAL_LINK: <tspan fill="#ffffff">SYNCHRONIZED</tspan> [0x7FF_A9B]
      </text>
      <text y="32" letter-spacing="1" opacity="0.8">
        &gt; ENCRYPTION : <tspan fill="#6aff8a">AES-256-GCM ACTIVE</tspan>
      </text>
      <text y="49" letter-spacing="1" opacity="0.8">
        &gt; BUFFER_SEQ : 01001000 01000101 01001100 01001100
      </text>
      <text y="66" letter-spacing="1" opacity="0.8">
        &gt; DIRECTORY  : /DEV/SHADOW // HELLBOY_ONLINE
      </text>
      <text y="83" letter-spacing="1.5" fill="#baffc9" font-weight="bold">
        &gt; MATRIX RUNTIME STATUS: STABLE [READY]
      </text>
    </g>

    <!-- ================================== -->
    <!-- RIGHT PANEL: GHOST OPERATIVE HERO  -->
    <!-- ================================== -->

    <!-- Tactical Operative Frame -->
    <g stroke="#00ff41" fill="none">
      <!-- High-Tech Frame Outline -->
      <rect x="710" y="60" width="455" height="495" rx="4"
            fill="#031206" fill-opacity="0.25"
            stroke="#00ff41" stroke-opacity="0.25" stroke-width="1"/>

      <!-- Tactical Corner Brackets (Right Panel) -->
      <path d="M 710 85 L 710 60 L 735 60" stroke="#00ff41" stroke-width="2.2" filter="url(#glow)"/>
      <path d="M 1140 60 L 1165 60 L 1165 85" stroke="#00ff41" stroke-width="2.2" filter="url(#glow)"/>
      <path d="M 710 530 L 710 555 L 735 555" stroke="#00ff41" stroke-width="2.2" filter="url(#glow)"/>
      <path d="M 1140 555 L 1165 555 L 1165 530" stroke="#00ff41" stroke-width="2.2" filter="url(#glow)"/>

      <!-- Side Calibration Ticks -->
      <line x1="706" y1="180" x2="714" y2="180" stroke="#00ff41" stroke-width="1.5"/>
      <line x1="706" y1="300" x2="716" y2="300" stroke="#00ff41" stroke-width="2"/>
      <line x1="706" y1="420" x2="714" y2="420" stroke="#00ff41" stroke-width="1.5"/>

      <line x1="1161" y1="180" x2="1169" y2="180" stroke="#00ff41" stroke-width="1.5"/>
      <line x1="1159" y1="300" x2="1169" y2="300" stroke="#00ff41" stroke-width="2"/>
      <line x1="1161" y1="420" x2="1169" y2="420" stroke="#00ff41" stroke-width="1.5"/>
    </g>

    <!-- Operative HUD Telemetry Header & Footer -->
    <g font-family="'Consolas', monospace" font-size="10.5" fill="#00ff41" letter-spacing="1.2">
      <!-- Top banner tags -->
      <rect x="726" y="74" width="180" height="20" rx="2" fill="#00ff41" fill-opacity="0.12"/>
      <text x="734" y="88" font-weight="bold" fill="#7dff9e">[OP: SHADOW-444]</text>

      <text x="1148" y="88" text-anchor="end" opacity="0.85">TACTICAL // NVG-4</text>

      <!-- Bottom telemetry tags -->
      <text x="726" y="542" fill="#6aff8a">OPTICS: ONLINE // 99.8%</text>
      <text x="1148" y="542" text-anchor="end" fill="#6aff8a">TARGET: LOCKED</text>
    </g>

    <!-- Concentric Target Reticle behind Operative Chest/Head -->
    <g transform="translate(935, 230)" fill="none" stroke="#00ff41" opacity="0.35">
      <circle r="120" stroke-width="0.8" stroke-dasharray="6 12">
        <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="40s" repeatCount="indefinite"/>
      </circle>
      <circle r="85" stroke-width="1" stroke-dasharray="40 10 5 10">
        <animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="25s" repeatCount="indefinite"/>
      </circle>
      <line x1="-130" y1="0" x2="-95" y2="0" stroke-width="1.2"/>
      <line x1="95" y1="0" x2="130" y2="0" stroke-width="1.2"/>
      <line x1="0" y1="-130" x2="0" y2="-95" stroke-width="1.2"/>
      <line x1="0" y1="95" x2="0" y2="130" stroke-width="1.2"/>
    </g>

    <!-- ================================== -->
    <!-- HERO IMAGE: GHOST OPERATIVE        -->
    <!-- ================================== -->
    <!--
      Standard Matrix Spec-Ops Operative:
      - Perfectly proportioned & centered in the right tactical frame (x=755, width=365, height=485)
      - Cybernetic Matrix Rim Glow highlighting the silhouette
      - Bottom fade mask feathering smoothly into the dark matrix floor
      - Base64 data URI guaranteeing flawless render in GitHub README and all local SVG previews
    -->
    <image
      id="ghost-operative"
      href="data:image/png;base64,{b64_data}"
      xlink:href="data:image/png;base64,{b64_data}"
      x="755"
      y="70"
      width="365"
      height="480"
      preserveAspectRatio="xMidYMid meet"
      filter="url(#cyberGlow)"
      mask="url(#ghostMask)"
    />

    <!-- Matrix Code Rain Layer Over Character Right Edge -->
    <g fill="#00ff41" font-family="'Consolas', monospace" font-size="14" opacity="0.6">
      <text x="1080" y="0">
        <tspan x="1080" dy="16">1</tspan><tspan x="1080" dy="16">0</tspan><tspan x="1080" dy="16">1</tspan>
        <tspan x="1080" dy="16">0</tspan><tspan x="1080" dy="16">0</tspan><tspan x="1080" dy="16">1</tspan>
        <tspan x="1080" dy="16">1</tspan>
        <animateTransform attributeName="transform" type="translate" values="0 -100; 0 550" dur="9s" repeatCount="indefinite"/>
      </text>
    </g>

    <!-- ================================== -->
    <!-- OUTER BORDER & CORNER ACCENTS      -->
    <!-- ================================== -->
    <g stroke="#00ff41" stroke-width="2" fill="none" filter="url(#glow)">
      <!-- Top-left outer bracket -->
      <path d="M 16 35 L 16 16 L 35 16"/>
      <!-- Top-right outer bracket -->
      <path d="M 1165 16 L 1184 16 L 1184 35"/>
      <!-- Bottom-left outer bracket -->
      <path d="M 16 565 L 16 584 L 35 584"/>
      <!-- Bottom-right outer bracket -->
      <path d="M 1165 584 L 1184 584 L 1184 565"/>
    </g>

    <!-- Corner Micro Indicators -->
    <g fill="#00ff41">
      <rect x="42" y="19" width="12" height="2"/>
      <rect x="42" y="23" width="6" height="2"/>
      <rect x="1146" y="19" width="12" height="2"/>
      <rect x="1152" y="23" width="6" height="2"/>
      <rect x="42" y="579" width="12" height="2"/>
      <rect x="42" y="575" width="6" height="2"/>
      <rect x="1146" y="579" width="12" height="2"/>
      <rect x="1152" y="575" width="6" height="2"/>
    </g>

    <!-- ================================== -->
    <!-- POST-PROCESSING OVERLAYS           -->
    <!-- ================================== -->

    <!-- CRT Scanlines Overlay -->
    <rect width="1200" height="600" fill="url(#scanlines)" pointer-events="none"/>

    <!-- Vignette Shadow Overlay -->
    <rect width="1200" height="600" fill="url(#vignette)" pointer-events="none"/>

    <!-- Animated Horizontal Cyber Scan Beam -->
    <rect x="0" y="0" width="1200" height="2" fill="#00ff41" opacity="0.35" filter="url(#glow)" pointer-events="none">
      <animate attributeName="y" values="-10; 610; -10" dur="8s" repeatCount="indefinite"/>
    </rect>

  </g>
</svg>'''

with open('profile.svg', 'w', encoding='utf-8') as f:
    f.write(svg_template)

print('Updated profile.svg successfully with Standard Matrix HUD Layout!')
