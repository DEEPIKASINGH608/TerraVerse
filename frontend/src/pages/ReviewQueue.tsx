import React from 'react';
import ReviewQueueItem, { QueueItemData } from '../components/review/ReviewQueueItem';

export const ReviewQueue: React.FC = () => {
  const queueItems: QueueItemData[] = [
    {
      id: 'Q-1',
      parcelId: 'SN-P-102',
      discrepancyType: 'Boundary Overlap (0.4m)',
      reason: 'Overlaps with adjacent parcel SN-P-103 along northern boundary line.',
      createdAt: '2026-10-07',
    },
    {
      id: 'Q-2',
      parcelId: 'SN-P-108',
      discrepancyType: 'Area Mismatch',
      reason: 'Revenue record states 910 m², drone survey geometry measures 850 m².',
      createdAt: '2026-10-07',
    },
  ];

  return (
    <div className="p-6 space-y-6 bg-slate-950 min-h-screen text-slate-100">
      <div>
        <h1 className="text-xl font-bold text-white">Manual Review Queue</h1>
        <p className="text-xs text-slate-400">Flagged items awaiting official surveyor confirmation</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {queueItems.map((item) => (
          <ReviewQueueItem key={item.id} item={item} onSelect={(id) => console.log('Selected item:', id)} />
        ))}
      </div>
    </div>
  );
};

export default ReviewQueue;