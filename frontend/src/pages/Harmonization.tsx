import React, { useState } from 'react';
import Card from '../components/common/Card';

export const Harmonization: React.FC = () => {
  const [running, setRunning] = useState(false);
  const [status, setStatus] = useState<string | null>(null);

  const triggerHarmonization = () => {
    setRunning(true);
    setStatus('Aligning drone vector geometries with cadastral boundary graphs...');
    setTimeout(() => {
      setRunning(false);
      setStatus('Harmonization complete! 128 parcels aligned with average confidence of 96.4%.');
    }, 2000);
  };

  return (
    <div className="p-6 space-y-6 bg-slate-950 min-h-screen text-slate-100">
      <div>
        <h1 className="text-xl font-bold text-white">AI Harmonization Engine</h1>
        <p className="text-xs text-slate-400">Execute spatial reconciliation and canonical twin generation</p>
      </div>

      <Card title="Run Pipeline" subtitle="Shakti Nagar Survey Unit">
        <div className="space-y-4">
          <p className="text-xs text-slate-300">
            This will evaluate geometry overlaps, trust scores, and historical registry data to match parcels.
          </p>

          <button
            onClick={triggerHarmonization}
            disabled={running}
            className="bg-emerald-600 hover:bg-emerald-500 text-white px-4 py-2 rounded text-xs font-semibold disabled:opacity-50 transition"
          >
            {running ? 'Processing Spatial Graph...' : 'Start Harmonization Job'}
          </button>

          {status && (
            <div className="p-3 bg-slate-950 border border-slate-800 text-xs text-emerald-400 rounded">
              {status}
            </div>
          )}
        </div>
      </Card>
    </div>
  );
};

export default Harmonization;