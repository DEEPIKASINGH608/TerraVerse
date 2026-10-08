import React from 'react';

export interface QueueItemData {
  id: string;
  parcelId: string;
  reason: string;
  discrepancyType: string;
  createdAt: string;
}

interface ReviewQueueItemProps {
  item: QueueItemData;
  onSelect: (parcelId: string) => void;
}

export const ReviewQueueItem: React.FC<ReviewQueueItemProps> = ({ item, onSelect }) => {
  return (
    <div
      className="p-4 bg-slate-900 border border-slate-800 rounded-lg hover:border-slate-700 transition cursor-pointer"
      onClick={() => onSelect(item.parcelId)}
    >
      <div className="flex items-center justify-between mb-2">
        <span className="font-bold text-sm text-white">{item.parcelId}</span>
        <span className="px-2 py-0.5 text-[10px] font-semibold bg-amber-500/10 text-amber-400 border border-amber-500/20 rounded">
          Needs Review
        </span>
      </div>
      <p className="text-xs text-slate-300 font-medium mb-1">{item.discrepancyType}</p>
      <p className="text-xs text-slate-400">{item.reason}</p>
      <p className="text-[10px] text-slate-500 mt-2">Flagged on {item.createdAt}</p>
    </div>
  );
};

export default ReviewQueueItem;