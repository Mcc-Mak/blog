import WalkingWorker from "../components/walking_worker";
function Home() {
  return (
    <div className="content home">
      <WalkingWorker />
      {/* Profile + resume */}
      <div className="profile">
        <img src={`${import.meta.env.BASE_URL}img/benny.png`} alt="Benny" className="profile-img" />
        <div className="resume">
          <h2>Mr. Mak Chun Wing (Benny), MScIT, MHKCS</h2>
          <hr />
          <h3>Summary</h3>
          <ul>
            <li>Strong sales and negotiation skills — securing deals with businesses and leading a small team to deliver IT solutions for construction corporations, generating 100k+ profits from the CityU Energy Research Team and Kai Tak MiC public housing IT projects.</li>
            <li>Deep understanding of the IT project lifecycle — from procurement and tender evaluation of technology solutions for 100+ startups and corporations in HK government work, to project management across various government IT and innovation projects.</li>
            <li>Research experience at the Intelligent Automation Centre in the UK and at local institutes, alongside algorithmic trading software support.</li>
            <li>Development experience across construction automation, robotics, autonomous driving, embedded systems and system communications, the Internet of Things, real-time data analytics and various I&amp;T government projects.</li>
            <li>Co-founder of the start-up TECHNI-BEAR — a self-motivated team player skilled in workflow systems, document management, automation, algorithmic design, robotics, IoT, data analytics and AI for business.</li>
            <li>Innovative, practical challenge-taker with strong communication skills, engaging a diverse audience — from international researchers, academics and company directors, to bankers, business clients and government officials.</li>
          </ul>
          <hr />
          <h3>Education</h3>
          <p><strong>Hong Kong Polytechnic University</strong> — Master of Science in Information Technology (Big Data and AI &amp; Fintech) (2021–2023)</p>
          <p><strong>City University of Hong Kong</strong> — Bachelor of Engineering (Honours) in Mechatronic Engineering (2014–2019)</p>
          <hr />
          <h3>Working Experience</h3>
          <h4>Electrical and Mechanical Services Department — Senior Information Technology Officer (Oct 2023 – Present)</h4>
          <p>Working with engineers in the Information Technology Development branch (ITD) of EMSD (Trading Fund) on projects spanning the Railway Branch, General Legislation Division and the Energy Efficiency Office (Regulatory Services). Drive the full software development lifecycle for government projects, manage vendors to meet deadlines for system design, implementation and review, and assist with procurement and budget administration for government services, in line with SPR and B/D circulars.</p>
          <h4>Electrical and Mechanical Services Department — Contract Programmer (Aug 2022 – Aug 2023)</h4>
          <p>Worked with engineers in the Railway Branch of EMSD (Regulatory Services), conducting the full software development cycle on government projects, managing vendors to meet deadlines for system implementation and review, and producing promotion videos for Geneva Prize-Winning Projects.</p>
          <h4>Industrial Centre, Hong Kong Polytechnic University — Assistant Engineer (Jun 2020 – Jul 2022)</h4>
          <p>Performed engineering duties in the Intelligent Automation and Robotic System division — assembling mechatronic systems with various mechanical tools and 3D drawings — and taught engineering students hands-on automation.</p>
          <ul>
            <li>Managed government IT and innovation projects and contractors, delivering results aligned with user requirements and expectations.</li>
            <li>Verified delivery of development projects against tender and contract requirements and compliance.</li>
            <li>Conducted IT project management across the entire SDLC, meeting deadlines, milestones and security guidelines.</li>
            <li>Handled government procurement and tendering of IT services and products for B/Ds in line with government compliance and regulations.</li>
          </ul>
          <strong>Related Projects:</strong>
          <ol>
            <li>Railway Incident Management System</li>
            <li>Central Electronic Record Keeping System (CERKS) for Confidential Workflow in STSAS</li>
            <li>STSAS</li>
            <li>Blockchain Record Management System (BRMS)</li>
            <li>IDAS/RDAS</li>
            <li>Security Risk Assessment &amp; Audit (SRAA)</li>
            <li>3D Point Cloud for Railway Defect Detection</li>
            <li>AIMS</li>
            <li>Document Management System – Fresh Water Cooling Tower</li>
            <li>Lift and Escalator Ordinance System (LEOS for Cap. 618)</li>
            <li>L&amp;E Condition Analysis System (LECAS)</li>
            <li>Railway Safety Monitoring System (Hong Kong MTR Station)</li>
            <li>Optical Character Recognition System for Mandatory Energy Efficiency Labelling Scheme (MEELS AI)</li>
          </ol>
          <p><strong>Main Duties:</strong> project administrator, SRAA management, tendering and procurement, system enhancement and development, system administration, budget and payment administration, communication and negotiation among B/Ds, contractors, internal sub-divisions and vendors, staff training and management, and sub-divisional funds and budget administration.</p>
          <h4>City University of Hong Kong — Research Assistant (Oct 2019 – May 2020)</h4>
          <p>Researched and developed the "gypsum block laying robot for the construction industry" — a government-funded project with building services and construction partners, building robot systems for 21st-century construction demand.</p>
          <h4>Horizon Software Asia Ltd. — Client Services Engineer Trainee (Mar – Jun 2019)</h4>
          <p>A multinational provider of algorithmic trading technology, serving clients ranging from investment banks to stock brokers.</p>
          <h4>Intelligent Automation Center, Loughborough University, UK — Research Intern (May – Aug 2018)</h4>
          <p>Assisted researchers on "Human–Robot Interaction in an Industrial Setting in VR", designing and developing robotic simulations for the project's VR experiments.</p>
          <h4>TECHNI-BEAR — Co-founder (Oct 2017 – Apr 2021)</h4>
          <p>Designed and delivered STEAM courses and STEAM-related services to schools and organizations — including Emanuel Primary School, Po Leung Kuk Yao Ling Sun College and Carmel Alison Lam Foundation Secondary School — reaching 100+ stakeholders.</p>
          <hr />
          <h3>Skills</h3>
          <p><strong>Technology:</strong> deep learning, financial trading systems, blockchain, VR, iOS mobile games, SLAM navigation, IoT, robotics, data analytics, mechatronic system design</p>
          <p><strong>Computer:</strong> Python, Unity C#, C/C++, Swift, Linux, Bash, HTML, CSS, JavaScript, ROS, RoboDK, MQTT, Bluetooth Low Energy, Solidity</p>
          <p><strong>Hardware:</strong> PLC, Arduino, Raspberry Pi, AutoCAD, SolidWorks, Jetson Board</p>
          <p><strong>Languages:</strong> Cantonese (Native), English (Fluent), Putonghua (Fluent)</p>
          <hr />
          <h3>Awards &amp; Certificates</h3>
          <ul>
            <li>2023 — Full Member (F-30527) Hong Kong Computer Society</li>
            <li>2022 — Microsoft Certified Azure AI Fundamentals</li>
            <li>2021 — Certificate of Getting Started with AI Jetson Nano Nvidia DLI</li>
            <li>2021 — Certificate of University Teaching PolyU</li>
            <li>2019 — HKIE Project Competition 1st Runner Up Scholarship Award</li>
            <li>2013 — W I Cheung Scholarship Participation Award</li>
            <li>2013–2014 — Outstanding Student Award (Po Leung Kuk Yao Ling Sun College)</li>
          </ul>
        </div>
      </div>
      {/* Contact links */}
      <div className="contact">
        <h3>Contact Me</h3>
        <div className="contact-links">
          <a href="https://mail.google.com/mail/?view=cm&fs=1&to=bennycwmak@gmail.com" target="_blank" rel="noopener noreferrer">
            <img src="https://cdn.jsdelivr.net/npm/simple-icons@v13/icons/gmail.svg" alt="Gmail" className="contact-icon" />
            <span>bennycwmak@gmail.com</span>
          </a>
          <a href="https://www.linkedin.com/in/chun-wing-mak-236125173/" target="_blank" rel="noopener noreferrer">
            <img src="https://cdn.jsdelivr.net/npm/simple-icons@v13/icons/linkedin.svg" alt="LinkedIn" className="contact-icon" />
            <span>Chun Wing Mak</span>
          </a>
          <a href="https://github.com/chunwmak9" target="_blank" rel="noopener noreferrer">
            <img src="https://cdn.jsdelivr.net/npm/simple-icons@v13/icons/github.svg" alt="GitHub" className="contact-icon" />
            <span>GitHub</span>
          </a>
          <a href="https://wa.me/85292671211" target="_blank" rel="noopener noreferrer">
            <img src="https://cdn.jsdelivr.net/npm/simple-icons@v13/icons/whatsapp.svg" alt="WhatsApp" className="contact-icon" />
            <span>+852 9267 1211</span>
          </a>
        </div>
      </div>
    </div>
  );
}
export default Home;