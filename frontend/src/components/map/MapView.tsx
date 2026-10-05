import React, { useEffect, useRef } from 'react';
import maplibregl from 'maplibre-gl';
import 'maplibre-gl/dist/maplibre-gl.css';

interface MapViewProps {
  onParcelSelect?: (parcelId: string) => void;
}

export const MapView: React.FC<MapViewProps> = ({ onParcelSelect }) => {
  const mapContainer = useRef<HTMLDivElement null |>(null);
  const map = useRef<maplibregl.Map | null>(null);

  useEffect(() => {
    if (map.current || !mapContainer.current) return;

    map.current = new maplibregl.Map({
      container: mapContainer.current,
      style: '[https://basemaps.cartocdn.com/gl/dark-matter-gl-style/style.json](https://basemaps.cartocdn.com/gl/dark-matter-gl-style/style.json)',
      center: [82.505, 25.005],
      zoom: 15
    });

    map.current.addControl(new maplibregl.NavigationControl(), 'top-right');

    map.current.on('load', () => {
      map.current?.addSource('shakti-parcels', {
        type: 'geojson',
        data: {
          type: 'FeatureCollection',
          features: [
            {
              type: 'Feature',
              properties: { id: 'SN-P-101', confidence: 0.96, status: 'harmonized' },
              geometry: {
                type: 'Polygon',
                coordinates: [[[82.500, 25.000], [82.501, 25.000], [82.501, 25.001], [82.500, 25.001], [82.500, 25.000]]]
              }
            },
            {
              type: 'Feature',
              properties: { id: 'SN-P-102', confidence: 0.65, status: 'needs_review' },
              geometry: {
                type: 'Polygon',
                coordinates: [[[82.501, 25.000], [82.502, 25.000], [82.502, 25.001], [82.501, 25.001], [82.501, 25.000]]]
              }
            }
          ]
        }
      });

      map.current?.addLayer({
        id: 'parcels-fill',
        type: 'fill',
        source: 'shakti-parcels',
        paint: {
          'fill-color': [
            'case',
            ['>=', ['get', 'confidence'], 0.90], '#10B981',
            '#EF4444'
          ],
          'fill-opacity': 0.5
        }
      });

      map.current?.addLayer({
        id: 'parcels-line',
        type: 'line',
        source: 'shakti-parcels',
        paint: {
          'line-color': '#FFFFFF',
          'line-width': 2
        }
      });

      map.current?.on('click', 'parcels-fill', (e) => {
        if (e.features && e.features[0]) {
          const pid = e.features[0].properties?.id;
          if (pid && onParcelSelect) onParcelSelect(pid);
        }
      });
    });
  }, [onParcelSelect]);

  return (
    <div className="relative w-full h-full">
      <div ref={mapContainer} className="w-full h-full rounded-lg overflow-hidden border border-slate-700" />
      <div className="absolute top-4 left-4 bg-slate-900/90 text-white p-3 rounded border border-slate-700 text-xs shadow-xl backdrop-blur">
        <p className="font-bold mb-1 text-slate-200">CONFIDENCE HEATMAP</p>
        <div className="flex items-center gap-2 mb-1">
          <span className="w-3 h-3 bg-emerald-500 rounded-full"></span>
          <span>Harmonized (&gt;= 0.90)</span>
        </div>
        <div className="flex items-center gap-2">
          <span className="w-3 h-3 bg-red-500 rounded-full"></span>
          <span>Needs Review (&lt; 0.90)</span>
        </div>
      </div>
    </div>
  );
};