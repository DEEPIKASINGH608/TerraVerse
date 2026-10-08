import React from 'react';
import Card from '../common/Card';
import Badge from '../common/Badge';
import { SpatialParcel } from '../../hooks/useSpatialData';

interface ParcelDetailsCardProps {
  parcel: SpatialParcel | null;
}

export const ParcelDetailsCard: React.FC<ParcelDetailsCardProps> = ({ parcel }) => {
  if (!parcel) {
    return (
      <Card title="Parcel Details">
        <p className="text-xs text-slate-500">Select a parcel on the map or list to view attributes.</p>
      </Card>
    );
  }

  const isHarmonized = parcel.status === 'harmonized';

  return (
    <Card title={`Parcel ${parcel.id}`} subtitle={`Khasra No: ${parcel.khasraNo}`}>
      <div className="space-y-4 text-xs">
        <div className="flex items-center justify-between">
          <span className="text-slate-400">Status:</span>
          <Badge
            label={parcel.status.replace('_', ' ').toUpperCase()}
            variant={isHarmonized ? 'success' : 'warning'}
          />
        </div>

        <div className="bg-slate-950 p-3 rounded-md border border-slate-800 space-y-2">
          <div className="flex justify-between">
            <span className="text-slate-400">Primary Owner:</span>
            <span className="text-slate-200 font-medium">{parcel.revenueOwner}</span>
          </div>
          <div className="flex justify-between">
            <span className="text-slate-400">Surveyed Area:</span>
            <span className="text-slate-200 font-medium">{parcel.areaSqm.toLocaleString()} m²</span>
          </div>
          <div className="flex justify-between">
            <span className="text-slate-400">AI Confidence:</span>
            <span className={parcel.confidence >= 0.9 ? 'text-emerald-400 font-bold' : 'text-amber-400 font-bold'}>
              {(parcel.confidence * 100).toFixed(0)}%
            </span>
          </div>
        </div>
      </div>
    </Card>
  );
};

export default ParcelDetailsCard;