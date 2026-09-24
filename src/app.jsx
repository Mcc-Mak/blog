import { useState } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Header from "./components/header";
import Navbar from "./components/navbar";
import Home from "./pages/home";
import Gallery from "./pages/gallery";
import Projects from "./pages/projects";
// Root layout: header + xp-tracking navbar + routed page content.
function App() {
  const [xp, setXp] = useState(0); // lifetime "XP to know me" counter
  const addXp = (points) => {
    setXp((current) => current + points);
  };
  return (
    <BrowserRouter basename="/blog">
      <div className="app">
        <Header />
        <Navbar xp={xp} addXp={addXp} />
        <main>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/projects" element={<Projects />} />
            <Route path="/gallery" element={<Gallery addXp={addXp} />} />
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  );
}
export default App;
