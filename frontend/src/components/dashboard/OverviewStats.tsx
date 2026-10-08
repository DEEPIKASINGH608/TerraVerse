import React from 'react';
import Card from '../common/Card';

interface MetricProps {
  label: string;
  value: string | number;
  change?: string;
  status?: 'good' | 'neutral' | 'bad';
}

export const OverviewStats: React.FC = () => {
  const metrics: MetricProps[] = [
    { label: 'Total Parcels', value: '1,284', change: '+12 this week', status: 'neutral' },
    { label: 'Harmonized Parcels', value: '1,140', change: '88.7% completed', status: 'good' },
    { label: 'Open Conflicts', value: '42', change: '-8 resolved today', status: 'good' },
    { label: 'Mean Precision', value: '±2.4 cm', change: 'GNSS Validated', status: 'neutral' },
  ];

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
      {metrics.map((m, idx) => (
        <Card key={idx}>
          <p className="text-xs text-slate-400 font-medium uppercase">{m.label}</p>
          <p className="text-2xl font-bold text-white mt-1">{m.value}</p>
          {m.change && (
            <p className={`text-xs mt-2 ${m.status === 'good' ? 'text-emerald-400' : 'text-slate-400'}`}>
              {m.change}
            </p>
          )}
        </Card>
      ))}
    </div>
  );
};

export default OverviewStats;