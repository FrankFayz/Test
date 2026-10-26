import { useEffect, useMemo, useState } from "react";
import { ArrowUpRight, Megaphone, Search, Sparkles } from "lucide-react";

const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

export default function App() {
  const [ads, setAds] = useState([]);
  const [query, setQuery] = useState("");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    fetch(`${API_URL}/api/ads/`)
      .then((response) => {
        if (!response.ok) throw new Error("The server returned an error.");
        return response.json();
      })
      .then(setAds)
      .catch(() => setError("We couldn't load advertisements. Make sure the backend is running, then refresh."))
      .finally(() => setLoading(false));
  }, []);

  const filteredAds = useMemo(() => {
    const term = query.trim().toLowerCase();
    if (!term) return ads;
    return ads.filter((ad) =>
      [ad.title, ad.business_name, ad.description, ad.category]
        .some((value) => value.toLowerCase().includes(term))
    );
  }, [ads, query]);

  const featured = filteredAds[0];

  return (
    <main className="page-shell">
      <nav className="nav wrap">
        <a className="brand" href="#" aria-label="AdSpot home">
          <span className="brand-icon"><Megaphone size={21} /></span>
          <span>ad<span className="brand-accent">spot</span></span>
        </a>
        <span className="nav-note"><span className="live-dot" /> A little inspiration, every day</span>
      </nav>

      <section className="hero wrap">
        <div className="hero-copy">
          <span className="eyebrow"><Sparkles size={15} /> THE GOOD STUFF IS HERE</span>
          <h1>Discover something <span>good.</span></h1>
          <p>A fresh space for great products, local businesses and offers worth a look.</p>
          <label className="search-box">
            <Search size={19} />
            <input
              aria-label="Search advertisements"
              placeholder="Search ads, brands or categories..."
              value={query}
              onChange={(event) => setQuery(event.target.value)}
            />
          </label>
        </div>
        <div className="hero-art" aria-hidden="true">
          <div className="orb orb-one" />
          <div className="orb orb-two" />
          <div className="art-card"><Megaphone size={62} strokeWidth={1.2} /></div>
          <span className="art-spark">✳</span>
          <span className="art-caption">GOOD THINGS<br />GET NOTICED.</span>
        </div>
      </section>

      <section className="wrap ads-section">
        <div className="section-heading">
          <div>
            <span className="eyebrow muted">A FEW GOOD FINDS</span>
            <h2>On the billboard</h2>
          </div>
          <span className="count-pill">{filteredAds.length} {filteredAds.length === 1 ? "advertisement" : "advertisements"}</span>
        </div>

        {loading && <p className="message">Getting the good stuff ready…</p>}
        {!loading && error && <p className="message error">{error}</p>}
        {!loading && !error && filteredAds.length === 0 && (
          <p className="message">No ads found. Try another search.</p>
        )}

        {!loading && !error && featured && (
          <article className="featured-card">
            <div className="featured-image" style={{ backgroundImage: `url("${featured.image_url}")` }}>
              <span className="featured-label"><Sparkles size={14} /> FEATURED FIND</span>
            </div>
            <div className="featured-content">
              <span className="category">{featured.category}</span>
              <h3>{featured.title}</h3>
              <p>{featured.description}</p>
              <span className="business-name">Presented by {featured.business_name}</span>
              {featured.link_url && (
                <a className="text-link" href={featured.link_url} target="_blank" rel="noreferrer">
                  Explore this offer <ArrowUpRight size={17} />
                </a>
              )}
            </div>
          </article>
        )}

        {!loading && !error && filteredAds.length > 1 && (
          <div className="ad-grid">
            {filteredAds.slice(1).map((ad) => (
              <article className="ad-card" key={ad.id}>
                <div className="card-image" style={{ backgroundImage: `url("${ad.image_url}")` }}>
                  <span className="category image-category">{ad.category}</span>
                </div>
                <div className="card-content">
                  <span className="business-name">{ad.business_name}</span>
                  <h3>{ad.title}</h3>
                  <p>{ad.description}</p>
                  {ad.link_url && (
                    <a className="text-link" href={ad.link_url} target="_blank" rel="noreferrer">
                      Take a look <ArrowUpRight size={16} />
                    </a>
                  )}
                </div>
              </article>
            ))}
          </div>
        )}
      </section>

      <footer className="footer wrap">
        <a className="brand footer-brand" href="#"><span className="brand-icon"><Megaphone size={18} /></span>ad<span className="brand-accent">spot</span></a>
        <span>A small billboard for big ideas.</span>
        <span>Built for learning ✦</span>
      </footer>
    </main>
  );
}
