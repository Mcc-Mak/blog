import ReactMarkdown from "react-markdown";
import { categories, projects } from "../data/projects";

// Resolve a relative project path against the Vite base (/blog/).
const assetUrl = (relativePath) => `${import.meta.env.BASE_URL}${relativePath}`;

function Projects() {
  return (
    <div className="content projects">
      <h1>Projects</h1>
      <p className="proj-legend">
        Role tags: 🧑&#xFE0F; Personal · 🎓 Academic · 🔬 Research · 📚 Learning ·
        🧪 Open-source
      </p>
      {categories.map((category) => {
        // Group projects by category, skipping empty ones.
        const categoryProjects = projects.filter(
          (project) => project.category === category.id
        );
        if (categoryProjects.length === 0) return null;
        return (
          <section key={category.id} className="proj-group">
            <h2>{category.name}</h2>
            <p className="proj-group-blurb">{category.blurb}</p>
            <div className="proj-grid">
              {categoryProjects.map((project) => (
                <article key={project.slug} className="proj-card">
                  {project.media.length > 0 && (
                    <div className="proj-media">
                      <img
                        src={assetUrl(project.media[0])}
                        alt={project.name}
                        loading="lazy"
                      />
                    </div>
                  )}
                  <div className="proj-body">
                    <h3>{project.name}</h3>
                    <div className="proj-tags">
                      {project.tags.map((tag) => (
                        <span key={tag} className="proj-tag">
                          {tag}
                        </span>
                      ))}
                      {project.tech.map((tech) => (
                        <span key={tech} className="proj-chip">
                          {tech}
                        </span>
                      ))}
                    </div>
                    <ReactMarkdown>{project.blurb}</ReactMarkdown>
                    <p className="proj-run">
                      <code>{project.runCommand}</code>
                    </p>
                    {project.media.length > 1 && (
                      <div className="proj-gallery">
                        {project.media.slice(1).map((mediaPath) => (
                          <img
                            key={mediaPath}
                            src={assetUrl(mediaPath)}
                            alt={`${project.name} screenshot`}
                            loading="lazy"
                          />
                        ))}
                      </div>
                    )}
                    <div className="proj-links">
                      <a href={project.source} target="_blank" rel="noopener noreferrer">
                        Source code ↗
                      </a>
                    </div>
                  </div>
                </article>
              ))}
            </div>
          </section>
        );
      })}
    </div>
  );
}

export default Projects;