import React from 'react';
import Card from '../components/common/Card';

export const Reports: React.FC = () => {
  return (
    <div className="p-6 space-y-6 bg-slate-950 min-h-screen text-slate-100">
      <div>
        <h1 className="text-xl font-bold text-white">Audit Reports & Export</h1>
        <p className="text-xs text-slate-400">Generate legal land registry summaries and spatial audit trails</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <Card title="Ward Summary PDF" subtitle="Complete harmonization audit report">
          <p className="text-xs text-slate-400 mb-4">Includes boundary confidence scores, resolved conflicts, and area variance tables.</p>
          <button className="bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 px-3 py-2 rounded text-xs">
            Export Ward PDF
          </button>
        </Card>

        <Card title="Canonical GeoJSON" subtitle="Harmonized spatial geometry export">
          <p className="text-xs text-slate-400 mb-4">Export high-precision land boundary geometries for GIS systems (EPSG:4326).</p>
          <button className="bg-emerald-600 hover:bg-emerald-500 text-white px-3 py-2 rounded text-xs font-semibold">
            Download GeoJSON
          </button>
        </Card>
      </div>
    </div>
  );
};

export default Reports;