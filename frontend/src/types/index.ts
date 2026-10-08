export interface GeoJSONGeometry {
  type: string;
  coordinates: any;
}

export interface SpatialParcel {
  id: string;
  parcel_id?: string;
  khasra_no?: string;
  muni_id?: string;
  owner_name?: string;
  land_use?: string;
  area_sqm?: number;
  geometry: GeoJSONGeometry;
  source_layer: 'drone' | 'revenue' | 'municipal';
}

export interface SpatialConflict {
  id: string;
  title: string;
  severity: 'low' | 'medium' | 'high' | 'critical';
  status: 'pending' | 'resolved' | 'escalated';
  conflict_type: 'overlap' | 'gap' | 'ownership_mismatch' | 'boundary_shift';
  parcel_a_id: string;
  parcel_b_id: string;
  overlap_area_sqm?: number;
  description: string;
  created_at: string;
}

export interface DashboardMetrics {
  total_parcels: number;
  resolved_conflicts: number;
  pending_conflicts: number;
  harmonization_progress: number;
  active_layers_count: number;
}