function WalkingWorker() {
  return (
    <div className="worker-bg" aria-hidden="true">
      <svg className="worker" viewBox="0 0 40 60" width="40" height="60">
        {/* Hard hat - peak pointing right */}
        <path d="M16 12 Q24 10 32 22 L34 22 Q34 16 24 12 Q16 14 14 22 Z" fill="#f5a623" stroke="#d4891a" strokeWidth="0.8" />
        <rect x="14" y="21" width="20" height="3" rx="1" fill="#f5a623" stroke="#d4891a" strokeWidth="0.5" />
        {/* Head */}
        <circle cx="22" cy="26" r="5" fill="#fdd" stroke="#c99" strokeWidth="0.5" />
        {/* Safety glasses */}
        <rect x="19" y="24" width="7" height="3" rx="1" fill="#555" opacity="0.6" />
        {/* Body / wiring suit vest */}
        <path d="M16 32 L16 48 L28 48 L28 32 Z" fill="#e8a87c" stroke="#c4805a" strokeWidth="0.8" />
        {/* Harness straps */}
        <line x1="18" y1="32" x2="18" y2="48" stroke="#f5a623" strokeWidth="1.5" />
        <line x1="26" y1="32" x2="26" y2="48" stroke="#f5a623" strokeWidth="1.5" />
        <line x1="16" y1="38" x2="28" y2="38" stroke="#f5a623" strokeWidth="1.5" />
        <line x1="16" y1="43" x2="28" y2="43" stroke="#f5a623" strokeWidth="1.5" />
        {/* Wiring / cable from harness trailing behind (left side) */}
        <path d="M18 35 Q12 38 10 44" fill="none" stroke="#333" strokeWidth="1" opacity="0.7" />
        <path d="M26 36 Q30 39 32 44" fill="none" stroke="#333" strokeWidth="1" opacity="0.6" />
        {/* Back arm (left, behind) */}
        <line className="arm back" x1="16" y1="34" x2="10" y2="40" stroke="#fdd" strokeWidth="2.5" strokeLinecap="round" />
        {/* Front arm (right, forward) */}
        <line className="arm front" x1="28" y1="34" x2="34" y2="40" stroke="#fdd" strokeWidth="2.5" strokeLinecap="round" />
        {/* Back leg (left) */}
        <g className="leg left">
          <line x1="18" y1="48" x2="16" y2="58" stroke="#555" strokeWidth="2.5" strokeLinecap="round" />
          <line x1="16" y1="58" x2="12" y2="59" stroke="#555" strokeWidth="2" strokeLinecap="round" />
        </g>
        {/* Front leg (right) */}
        <g className="leg right">
          <line x1="26" y1="48" x2="28" y2="58" stroke="#555" strokeWidth="2.5" strokeLinecap="round" />
          <line x1="28" y1="58" x2="32" y2="59" stroke="#555" strokeWidth="2" strokeLinecap="round" />
        </g>
        {/* Safety boots */}
        <rect x="10" y="57" width="5" height="3" rx="1" fill="#8B4513" />
        <rect x="29" y="57" width="5" height="3" rx="1" fill="#8B4513" />
      </svg>
    </div>
  );
}

export default WalkingWorker;
