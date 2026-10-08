import React from 'react';
import MapView from '../components/map/MapView';
import ParcelDetailsCard from '../components/parcels/ParcelDetailsCard';
import useSpatialData from '../hooks/useSpatialData';

export const MapWorkspace: React.FC = () => {
  const { selectedParcel, setSelectedParcelId } = useSpatialData();

  return (
    <div className="flex h-screen bg-slate-950 text-slate-100">
      <div className="flex-1 relative p-4">
        <MapView onParcelSelect={(id) => setSelectedParcelId(id)} />
      </div>
      <div className="w-96 p-4 border-l border-slate-800 bg-slate-900 overflow-y-auto">
        <ParcelDetailsCard parcel={selectedParcel} />
      </div>
    </div>
  );
};

export default MapWorkspace;