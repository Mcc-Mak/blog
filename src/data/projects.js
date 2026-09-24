// Single source of truth for the Projects page:
// category groupings, project cards, run commands, media and source links.
export const categories = [
  {
    id: "trading",
    name: "Trading & Fintech",
    blurb: "Market dashboards, algorithmic trading and stock analysis tools.",
  },
  {
    id: "robotics",
    name: "Robotics & Automation",
    blurb: "Industrial robots, non-destructive testing and automation research.",
  },
  {
    id: "computer_vision",
    name: "Computer Vision & Media",
    blurb: "Face landmark detection and image/video processing utilities.",
  },
  {
    id: "embedded_iot",
    name: "Embedded & IoT",
    blurb: "ESP32 / M5Stack firmware and hardware experiments.",
  },
  {
    id: "web",
    name: "Web Development",
    blurb: "Websites and web apps built with Python frameworks.",
  },
  {
    id: "games",
    name: "Games",
    blurb: "Desktop and mobile games built with Pygame and Unity.",
  },
  {
    id: "algorithms",
    name: "Algorithms & Libraries",
    blurb: "Algorithm implementations and reusable code libraries.",
  },
];
// Portfolio showcase entries — keep in sync with the root README toctree.
export const projects = [
  {
    slug: "automated_trading_robot",
    name: "Automated Trading Robot",
    category: "trading",
    tags: ["Personal"],
    tech: ["Python"],
    runCommand: "python stock_app.py",
    source: "https://github.com/chunwmak9/Automated_Trading_Robot",
    media: [],
    blurb:
      "Algorithmic trading robot for the Hong Kong and US stock markets. During market hours the dashboard runs the bot and shows buy/sell advice points, with the running gain or loss from the bot's advice plus technical info about each stock token.",
  },
  {
    slug: "us_stock_scanner",
    name: "US Stock Scanner",
    category: "trading",
    tags: ["Personal"],
    tech: ["Python", "Sentiment Analysis", "Data Analysis"],
    runCommand: "python stock_gui.py",
    source: "https://github.com/chunwmak9/US_Stock_Scanner",
    media: [
      "projects/us_stock_scanner/search_window.png",
      "projects/us_stock_scanner/stock_selection.png",
      "projects/us_stock_scanner/stock_analysis.png",
    ],
    blurb:
      "Stock data analyzer that helps users pick high-potential stocks: sentiment analysis based on recent news combined with statistical analysis of historical price data.",
  },
  {
    slug: "jenga_ur_robot",
    name: "Jenga UR-10 Robot",
    category: "robotics",
    tags: ["Academic"],
    tech: ["UR-10", "URScript", "3D Printing"],
    runCommand: "URScript program on the UR-10 controller",
    source: "https://github.com/chunwmak9/Jenga_UR_Robot",
    media: [
      "projects/jenga_ur_robot/ur_jenga.gif",
      "projects/jenga_ur_robot/ur_coordinate1.jpg",
      "projects/jenga_ur_robot/ur_coordinate2.jpg",
      "projects/jenga_ur_robot/ur_coordinate3.jpg",
    ],
    blurb:
      "A UR-10 industrial robot stacks 18 layers of Jenga blocks written in URScript. It picks blocks with 3D-printed mount holders from a work table and places them in a loop until the tower is complete.",
  },
  {
    slug: "sound_processing",
    name: "Tile Void NDT Robot",
    category: "robotics",
    tags: ["Research"],
    tech: ["Python", "MATLAB", "Arduino", "Bluetooth HC-05"],
    runCommand: "Python GUI on PC + solenoid hammer / microphone robot hardware",
    source: "https://github.com/chunwmak9/SoundProcessing",
    media: ["projects/sound_processing/test.jpg"],
    blurb:
      "Non-destructive test robot for tile voids: a solenoid hammer impacts the tile wall, a uni-directional microphone captures the response, and frequency-segment algorithms classify hollow vs solid areas in about 1 second. The robot repositions over the next tile via Bluetooth + Arduino.",
  },
  {
    slug: "face_point_detector_68",
    name: "68-Point Face Detector",
    category: "computer_vision",
    tags: ["Academic"],
    tech: ["Python", "Computer Vision"],
    runCommand: "Python API",
    source: "https://github.com/chunwmak9/face_point_detector_68",
    media: ["projects/face_point_detector_68/face_points.png"],
    blurb:
      "Face detector that returns 68 facial landmark points, indexed 0 to 67, for face alignment and tracking.",
  },
  {
    slug: "image_processing_tools",
    name: "Image Processing Tools",
    category: "computer_vision",
    tags: ["Personal"],
    tech: ["Python", "OpenCV"],
    runCommand: "Python API",
    source: "https://github.com/chunwmak9/image_processing_tools",
    media: [
      "projects/image_processing_tools/panorama.jpg",
      "projects/image_processing_tools/wall_paint.mov",
    ],
    blurb:
      "Image processing toolkit providing easy APIs for common operations — convert a video into a panorama image, pixelate an image, and more.",
  },
  {
    slug: "m5stack",
    name: "M5Stack Firmware Fork",
    category: "embedded_iot",
    tags: ["Open-source"],
    tech: ["C++", "ESP32", "Arduino"],
    runCommand: "Arduino IDE / PlatformIO",
    source: "https://github.com/chunwmak9/M5Stack",
    media: [],
    blurb:
      "Fork of the official M5Stack (ESP32) Arduino library with a custom UHF RFID fix, used as the base for M5Stack Core experiments.",
  },
  {
    slug: "personal_web",
    name: "Personal Web (Django)",
    category: "web",
    tags: ["Personal"],
    tech: ["Django", "Python", "HTML/CSS"],
    runCommand: "python django_web/manage.py runserver (after pip install django pillow)",
    source: "https://github.com/chunwmak9/Personal_web",
    media: [
      "projects/personal_web/home.png",
      "projects/personal_web/resume.png",
      "projects/personal_web/blog.png",
    ],
    blurb:
      "Personal website built with the Django framework — Home, Resume and Blog sections. An earlier generation of this blog, now superseded by the React version you are reading.",
  },
  {
    slug: "skywar",
    name: "SkyWar",
    category: "games",
    tags: ["Personal"],
    tech: ["Python", "Pygame"],
    runCommand: "python user_interface.py",
    source: "https://github.com/chunwmak9/SkyWar",
    media: [],
    blurb:
      "Sky shooting game written in Pygame. The player flies a fighter aircraft, choosing to escape incoming missiles or fight back by shooting bullets.",
  },
  {
    slug: "treasury_hunter_ios",
    name: "Treasury Hunter (iOS)",
    category: "games",
    tags: ["Personal"],
    tech: ["Unity", "C#", "iOS", "Gyroscope"],
    runCommand: "Unity build on iPhone (tested on iPhone 13 Pro Max)",
    source: "https://github.com/chunwmak9/Treasury_Hunter_IOS",
    media: [
      "projects/treasury_hunter_ios/main_menu.png",
      "projects/treasury_hunter_ios/main.png",
      "projects/treasury_hunter_ios/object_collision.png",
      "projects/treasury_hunter_ios/end_game.png",
    ],
    blurb:
      "Unity game for iOS: aim by tilting the phone with the gyroscope, hit treasure boxes for +1 score and avoid bombs for a −3 penalty, against a 60-second countdown.",
  },
  {
    slug: "python_basic_algorithms",
    name: "Python Basic Algorithms",
    category: "algorithms",
    tags: ["Learning"],
    tech: ["Python", "Algorithms"],
    runCommand: "Python modules",
    source: "https://github.com/chunwmak9/Python_Basic_Algorithms",
    media: [],
    blurb:
      "Algorithm library with quick implementations: bucket sort, bubble sort, graph concepts and data structures (adjacency matrix/list, complement, transpose, line and dual graphs) and depth-first search.",
  },
];