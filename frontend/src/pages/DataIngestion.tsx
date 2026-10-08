import React, { useState } from 'react';
import DatasetUploader from '../components/datasets/DatasetUploader';
import Card from '../components/common/Card';

export const DataIngestion: React.FC = () => {
  const [ingestedFiles, setIngestedFiles] = useState<string[]>(['revenue_records_2012.geojson']);

  return (
    <div className="p-6 space-y-6 bg-slate-950 min-h-screen text-slate-100">
      <div>
        <h1 className="text-xl font-bold text-white">Data Ingestion Hub</h1>
        <p className="text-xs text-slate-400">Import spatial datasets, drone boundary polygons, and cadastral maps</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <DatasetUploader onUploadSuccess={(file) => setIngestedFiles((prev) => [...prev, file])} />

        <Card title="Active Ingested Layers">
          <ul className="space-y-2 text-xs">
            {ingestedFiles.map((f, i) => (
              <li key={i} className="flex justify-between p-2 bg-slate-950 rounded border border-slate-800">
                <span className="text-slate-200 font-mono">{f}</span>
                <span className="text-emerald-400 font-semibold">Active</span>
              </li>
            ))}
          </ul>
        </Card>
      </div>
    </div>
  );
};

export default DataIngestion;