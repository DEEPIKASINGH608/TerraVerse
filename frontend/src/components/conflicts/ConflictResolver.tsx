import React from 'react';
import Badge from '../common/Badge';
import Card from '../common/Card';

export interface ConflictItem {
  id: string;
  khasraNo: string;
  type: 'Boundary Overlap' | 'Ownership Mismatch' | 'Area Discrepancy';
  severity: 'high' | 'medium' | 'low';
  revenueOwner: string;
  droneAreaSqm: number;
  recordedAreaSqm: number;
}

interface ConflictResolverProps {
  conflict: ConflictItem;
  onResolve: (id: string, resolution: 'accept_drone' | 'accept_revenue') => void;
}

export const ConflictResolver: React.FC<ConflictResolverProps> = ({ conflict, onResolve }) => {
  const getBadgeVariant = (severity: string) => {
    if (severity === 'high') return 'danger';
    if (severity === 'medium') return 'warning';
    return 'info';
  };

  return (
    <Card title={`Conflict Resolution #${conflict.id}`} subtitle={`Khasra No: ${conflict.khasraNo}`}>
      <div className="space-y-4">
        <div className="flex items-center justify-between">
          <span className="text-xs text-slate-400">Issue Type: {conflict.type}</span>
          <Badge label={conflict.severity.toUpperCase()} variant={getBadgeVariant(conflict.severity)} />
        </div>

        <div className="grid grid-cols-2 gap-3 bg-slate-950 p-3 rounded-md border border-slate-800 text-xs">
          <div>
            <p className="text-slate-500 uppercase font-semibold text-[10px]">Revenue Records</p>
            <p className="text-slate-200 font-medium mt-1">Owner: {conflict.revenueOwner}</p>
            <p className="text-slate-400">Area: {conflict.recordedAreaSqm} m²</p>
          </div>
          <div>
            <p className="text-slate-500 uppercase font-semibold text-[10px]">Drone Survey (2026)</p>
            <p className="text-slate-200 font-medium mt-1">Precision: ±2cm</p>
            <p className="text-slate-400">Extracted Area: {conflict.droneAreaSqm} m²</p>
          </div>
        </div>

        <div className="flex gap-2 pt-2">
          <button
            onClick={() => onResolve(conflict.id, 'accept_drone')}
            className="flex-1 bg-emerald-600 hover:bg-emerald-500 text-white text-xs py-2 px-3 rounded font-medium transition"
          >
            Accept Drone Geometry
          </button>
          <button
            onClick={() => onResolve(conflict.id, 'accept_revenue')}
            className="flex-1 bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs py-2 px-3 rounded font-medium border border-slate-700 transition"
          >
            Keep Revenue Record
          </button>
        </div>
      </div>
    </Card>
  );
};

export default ConflictResolver;