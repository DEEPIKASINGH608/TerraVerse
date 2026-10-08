import React from 'react';
import OverviewStats from '../components/dashboard/OverviewStats';
import Card from '../components/common/Card';

export const Dashboard: React.FC = () => {
  return (
    <div className="p-6 space-y-6 bg-slate-950 min-h-screen text-slate-100">
      <div>
        <h1 className="text-xl font-bold text-white">Shakti Nagar Ward Overview</h1>
        <p className="text-xs text-slate-400">Spatial data harmonization & AI discrepancy dashboard</p>
      </div>

      <OverviewStats />

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <Card title="Harmonization Progress by Block">
          <div className="space-y-3 text-xs">
            <div>
              <div className="flex justify-between mb-1">
                <span className="text-slate-300">Block A (Residential)</span>
                <span className="text-emerald-400 font-bold">94%</span>
              </div>
              <div className="w-full bg-slate-800 h-2 rounded-full overflow-hidden">
                <div className="bg-emerald-500 h-full w-[94%]" />
              </div>
            </div>
            <div>
              <div className="flex justify-between mb-1">
                <span className="text-slate-300">Block B (Commercial Zone)</span>
                <span className="text-amber-400 font-bold">78%</span>
              </div>
              <div className="w-full bg-slate-800 h-2 rounded-full overflow-hidden">
                <div className="bg-amber-500 h-full w-[78%]" />
              </div>
            </div>
          </div>
        </Card>

        <Card title="Recent Engine Actions">
          <ul className="text-xs space-y-2 text-slate-300">
            <li className="flex justify-between py-1 border-b border-slate-800/60">
              <span>Auto-harmonized 14 parcels in Ward 12</span>
              <span className="text-slate-500">10m ago</span>
            </li>
            <li className="flex justify-between py-1 border-b border-slate-800/60">
              <span>Flagged overlap on Parcel SN-P-102</span>
              <span className="text-slate-500">22m ago</span>
            </li>
            <li className="flex justify-between py-1">
              <span>Drone vector batch ingest completed</span>
              <span className="text-slate-500">1h ago</span>
            </li>
          </ul>
        </Card>
      </div>
    </div>
  );
};

export default Dashboard;