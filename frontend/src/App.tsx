import React, { useState } from 'react';
import MapView from './components/map/MapView';
import { Layers, Play } from 'lucide-react';
import axios from 'axios';

export const App: React.FC = () => {
  const [selectedParcel, setSelectedParcel] = useState<string | null>("SN-P-101");
  const [demoStatus, setDemoStatus] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  const runOneClickDemo = async () => {
    setLoading(true);
    setDemoStatus("Running Shakti Nagar AI Harmonization Engine...");
    try {
      const res = await axios.post("http://localhost:8000/api/v1/demo/run");
      setDemoStatus(
        `✓ Demo Completed! Auto-Harmonized: ${res.data.auto_harmonized} | Conflicts Flagged: ${res.data.flagged_for_review}`
      );
    } catch (err: unknown) {
      if (axios.isAxiosError(err)) {
        setDemoStatus(`Demo Error: ${err.message}`);
      } else {
        setDemoStatus(`Demo Error: ${String(err)}`);
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col h-screen bg-slate-950 text-slate-100 font-sans">
      {/* Top Header */}
      <header className="h-16 bg-slate-900 border-b border-slate-800 px-6 flex items-center justify-between">
        <div className="flex items-center gap-3">
          <div className="p-2 bg-emerald-500/10 rounded-lg border border-emerald-500/20">
            <Layers className="w-6 h-6 text-emerald-400" />
          </div>
          <div>
            <h1 className="font-bold text-lg text-white">TERRAVERSE AI</h1>
            <p className="text-xs text-slate-400">Urban Land Record Harmonization Platform</p>
          </div>
        </div>

        <div className="flex items-center gap-4">
          <button
            onClick={runOneClickDemo}
            disabled={loading}
            className="flex items-center gap-2 bg-emerald-600 hover:bg-emerald-500 text-white px-4 py-2 rounded-md font-semibold text-sm transition shadow-lg disabled:opacity-50"
          >
            <Play className="w-4 h-4" />
            {loading ? "Processing..." : "RUN SHAKTI NAGAR DEMO"}
          </button>
        </div>
      </header>

      {/* Main Workspace Layout */}
      <div className="flex flex-1 overflow-hidden">
        {/* Map View Area */}
        <main className="flex-1 p-4 relative">
          <MapView onParcelSelect={(id) => setSelectedParcel(id)} />
          {demoStatus && (
            <div className="absolute bottom-6 left-6 right-6 bg-slate-900/95 border border-emerald-500/30 text-emerald-300 p-3 rounded text-sm shadow-2xl backdrop-blur">
              {demoStatus}
            </div>
          )}
        </main>

        {/* Parcel Details Sidebar */}
        <aside className="w-96 bg-slate-900 border-l border-slate-800 p-6 flex flex-col gap-6 overflow-y-auto">
          <div>
            <h2 className="text-sm font-bold text-slate-400 uppercase tracking-wider mb-2">Selected Parcel</h2>
            <div className="bg-slate-800/50 p-4 rounded-lg border border-slate-700">
              <span className="text-2xl font-extrabold text-emerald-400">{selectedParcel || "Select Parcel"}</span>
              <p className="text-xs text-slate-400 mt-1">Shakti Nagar Ward #12</p>
            </div>
          </div>

          <div>
            <h2 className="text-sm font-bold text-slate-400 uppercase tracking-wider mb-3">Multi-Source Evidence</h2>
            <div className="space-y-3">
              <div className="p-3 bg-slate-800/30 rounded border border-slate-700/50">
                <div className="flex justify-between text-xs font-semibold">
                  <span className="text-slate-300">Revenue Dept (2012)</span>
                  <span className="text-emerald-400">0.90 Trust</span>
                </div>
                <p className="text-xs text-slate-400 mt-1">Area: 1,250 sqm | Owner: Owner_101</p>
              </div>

              <div className="p-3 bg-slate-800/30 rounded border border-slate-700/50">
                <div className="flex justify-between text-xs font-semibold">
                  <span className="text-slate-300">Drone Survey (2026)</span>
                  <span className="text-emerald-400">0.98 Trust</span>
                </div>
                <p className="text-xs text-slate-400 mt-1">Area: 1,268 sqm | Precision: ±2cm</p>
              </div>
            </div>
          </div>

          <div className="bg-slate-800/40 p-4 rounded-lg border border-slate-700">
            <span className="text-xs text-slate-400 font-bold uppercase">Harmonization Confidence</span>
            <div className="flex items-baseline gap-2 mt-2">
              <span className="text-3xl font-black text-emerald-400">0.96</span>
              <span className="text-xs text-emerald-500 font-bold">HIGH CONFIDENCE</span>
            </div>
            <p className="text-xs text-slate-400 mt-2">Automatically harmonized into canonical twin.</p>
          </div>
        </aside>
      </div>
    </div>
  );
};

export default App;