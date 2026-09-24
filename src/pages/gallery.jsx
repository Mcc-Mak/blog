import { useEffect, useState } from "react";
import ReactMarkdown from "react-markdown";

function Gallery({ addXp }) {
  const [sections, setSections] = useState([]);
  const [open, setOpen] = useState({});
  const [xpPop, setXpPop] = useState(null);

  useEffect(() => {
    fetch(`${import.meta.env.BASE_URL}gallery.md`)
      .then((res) => res.text())
      .then((text) => {
        const rawBlocks = text.split(/(?=^## )/m);
        const parsedSections = rawBlocks
          .map((block) => {
            const lines = block.trim().split("\n");
            const title = lines.find((line) => line.startsWith("## "));
            const content = lines
              .filter((line) => !line.startsWith("## "))
              .join("\n")
              .trim();
            return { title: title ? title.replace("## ", "") : null, content };
          })
          .filter((section) => section.title);
        setSections(parsedSections);
      });
  }, []);

  const toggle = (index) => {
    setOpen((prev) => ({ ...prev, [index]: !prev[index] }));
    if (!open[index]) {
      addXp(30);
      setXpPop(index);
      setTimeout(() => setXpPop(null), 400);
    }
  };

  return (
    <div className="content gallery">
      <h1>Gallery</h1>
      {sections.map((section, index) => (
        <div key={index} className={`gallery-block ${open[index] ? "open" : ""}`}>
          <button className="gallery-toggle" onClick={() => toggle(index)}>
            <span className="gallery-arrow">{open[index] ? "▼" : "▶"}</span>
            {section.title}
            {xpPop === index && <span className="xp-fly">+30XP</span>}
          </button>
          <div className="gallery-body">
            <ReactMarkdown>{section.content}</ReactMarkdown>
          </div>
        </div>
      ))}
    </div>
  );
}

export default Gallery;
