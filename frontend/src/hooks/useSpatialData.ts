import { useState, useEffect, useCallback } from 'react';
import axios from 'axios';

export interface SpatialParcel {
  id: string;
  khasraNo: string;
  status: 'harmonized' | 'needs_review' | 'pending';
  confidence: number;
  revenueOwner: string;
  areaSqm: number;
  coordinates: number[][][];
}

export const useSpatialData = () => {
  const [parcels, setParcels] = useState<SpatialParcel[]>([]);
  const [selectedParcelId, setSelectedParcelId] = useState<string | null>(null);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  const fetchParcels = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await axios.get('http://localhost:8000/api/v1/parcels');
      setParcels(response.data);
    } catch (err: unknown) {
      if (axios.isAxiosError(err)) {
        setError(err.message);
      } else {
        setError('Failed to fetch spatial data');
      }
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchParcels();
  }, [fetchParcels]);

  const selectedParcel = parcels.find((p) => p.id === selectedParcelId) || null;

  return {
    parcels,
    selectedParcel,
    selectedParcelId,
    setSelectedParcelId,
    loading,
    error,
    refetch: fetchParcels,
  };
};

export default useSpatialData;