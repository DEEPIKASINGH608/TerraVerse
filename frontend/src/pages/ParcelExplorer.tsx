import React, { useState } from 'react';
import Card from '../components/common/Card';
import Badge from '../components/common/Badge';

export const ParcelExplorer: React.FC = () => {
  const [searchTerm, setSearchTerm] = useState('');

  const sampleParcels = [
    { id: 'SN-P-101', khasra: '101/A', owner: 'Ramesh Chand', area: 1250, status: 'harmonized' },
    { id: 'SN-P-102', khasra: '102/B', owner: 'Suresh Verma', area: 1268, status: 'needs_review' },
    { id: 'SN-P-103', khasra: '103/A', owner: 'Priya Sharma', area: 980, status: 'harmonized' },
  ];

  const filtered = sampleParcels.filter(
    (p) => p.id.toLowerCase().includes(searchTerm.toLowerCase()) || p.owner.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="p-6 space-y-6 bg-slate-950 min-h-screen text-slate-100">
      <div>
        <h1 className="text-xl font-bold text-white">Parcel Explorer</h1>
        <p className="text-xs text-slate-400">Search and filter recorded land parcels</p>
      </div>

      <Card>
        <input
          type="text"
          placeholder="Search by Parcel ID or Owner..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          className="w-full bg-slate-950 border border-slate-800 rounded px-3 py-2 text-xs text-white focus:outline-none focus:border-emerald-500 mb-4"
        />

        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs text-slate-300">
            <thead className="bg-slate-950 text-slate-500 uppercase text-[10px]">
              <tr>
                <th className="p-2">Parcel ID</th>
                <th className="p-2">Khasra No</th>
                <th className="p-2">Owner</th>
                <th className="p-2">Area (m²)</th>
                <th className="p-2">Status</th>
              </tr>
            </thead>
            <tbody>
              {filtered.map((p) => (
                <tr key={p.id} className="border-b border-slate-800/50 hover:bg-slate-800/30">
                  <td className="p-2 font-mono text-emerald-400">{p.id}</td>
                  <td className="p-2">{p.khasra}</td>
                  <td className="p-2">{p.owner}</td>
                  <td className="p-2">{p.area}</td>
                  <td className="p-2">
                    <Badge label={p.status} variant={p.status === 'harmonized' ? 'success' : 'warning'} size="sm" />
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </Card>
    </div>
  );
};

export default ParcelExplorer;