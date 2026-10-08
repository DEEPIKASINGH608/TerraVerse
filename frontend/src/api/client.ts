import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api/v1';

export const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const fetchParcels = async () => {
  const response = await apiClient.get('/parcels');
  return response.data;
};

export const fetchConflicts = async () => {
  const response = await apiClient.get('/conflicts');
  return response.data;
};

export const fetchDashboardMetrics = async () => {
  const response = await apiClient.get('/pipeline/metrics');
  return response.data;
};

export const uploadDataset = async (formData: FormData) => {
  const response = await apiClient.post('/ingest/upload', formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  });
  return response.data;
};