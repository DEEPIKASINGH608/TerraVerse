import React, { useState } from 'react';
import ConflictResolver, { ConflictItem } from '../components/conflicts/ConflictResolver';

export const Conflicts: React.FC = () => {
  const [conflicts, setConflicts] = useState<ConflictItem[]>([
    {
      id: 'CONF-001',
      khasraNo: '102/B',
      type: 'Boundary Overlap',
      severity: 'high',
      revenueOwner: 'Suresh Verma',
      droneAreaSqm: 1268,
      recordedAreaSqm: 1210,
    },
    {
      id: 'CONF-002',
      khasraNo: '108/A',
      type: 'Area Discrepancy',
      severity: 'medium',
      revenueOwner: 'Anil Kumar',
      droneAreaSqm: 850,
      recordedAreaSqm: 910,
    },
  ]);

  const handleResolve = (id: string, resolution: string) => {
    setConflicts((prev) => prev.filter((c) => c.id !== id));
    console.log(`Resolved ${id} using strategy: ${resolution}`);
  };

  return (
    <div className="p-6 space-y-6 bg-slate-950 min-h-screen text-slate-100">
      <div>
        <h1 className="text-xl font-bold text-white">Spatial & Attribute Conflicts</h1>
        <p className="text-xs text-slate-400">Review conflicts flagged during the harmonization pipeline</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {conflicts.map((conflict) => (
          <ConflictResolver key={conflict.id} conflict={conflict} onResolve={handleResolve} />
        ))}
        {conflicts.length === 0 && (
          <div className="col-span-2 text-center py-12 text-slate-500 text-sm">
            ✓ All conflicts resolved for this ward!
          </div>
        )}
      </div>
    </div>
  );
};

export default Conflicts;