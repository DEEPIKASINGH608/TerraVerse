import React, { useState } from 'react';
import Card from '../common/Card';

interface DatasetUploaderProps {
  onUploadSuccess?: (filename: string) => void;
}

export const DatasetUploader: React.FC<DatasetUploaderProps> = ({ onUploadSuccess }) => {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [uploading, setUploading] = useState(false);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      setSelectedFile(e.target.files[0]);
    }
  };

  const handleUpload = () => {
    if (!selectedFile) return;
    setUploading(true);

    // Simulate upload delay
    setTimeout(() => {
      setUploading(false);
      if (onUploadSuccess) onUploadSuccess(selectedFile.name);
      setSelectedFile(null);
    }, 1200);
  };

  return (
    <Card title="Spatial Data Ingestion" subtitle="Upload GeoJSON, KML, or CSV control points">
      <div className="space-y-4">
        <div className="border-2 border-dashed border-slate-700 rounded-lg p-6 text-center hover:border-emerald-500/50 transition">
          <input
            type="file"
            accept=".geojson,.json,.csv,.kml"
            onChange={handleFileChange}
            className="hidden"
            id="spatial-file-input"
          />
          <label htmlFor="spatial-file-input" className="cursor-pointer space-y-2 block">
            <p className="text-xs text-slate-300 font-medium">
              {selectedFile ? selectedFile.name : 'Click to browse spatial files'}
            </p>
            <p className="text-[10px] text-slate-500">Supports GeoJSON, CSV (EPSG:4326)</p>
          </label>
        </div>

        {selectedFile && (
          <button
            onClick={handleUpload}
            disabled={uploading}
            className="w-full bg-emerald-600 hover:bg-emerald-500 text-white text-xs py-2.5 rounded font-semibold transition disabled:opacity-50"
          >
            {uploading ? 'Ingesting Layer...' : `Ingest ${selectedFile.name}`}
          </button>
        )}
      </div>
    </Card>
  );
};

export default DatasetUploader;