'use client';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import L from 'leaflet';

const icon = L.icon({
  iconUrl: 'https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon.png',
  iconRetinaUrl: 'https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon-2x.png',
  shadowUrl: 'https://unpkg.com/leaflet@1.9.4/dist/images/marker-shadow.png',
  iconSize: [25,41], iconAnchor: [12,41],
});
(L.Marker as any).prototype.options.icon = icon;

export default function MapView({ lat, lon, label='Current Position' }:{ lat:number; lon:number; label?:string }) {
  if (typeof window === 'undefined') return null;
  const center: [number, number] = [lat || 25.276987, lon || 55.296249];
  return (
    <div className="rounded-2xl overflow-hidden border shadow">
      <MapContainer center={center} zoom={5} style={{ height: '360px', width: '100%' }} scrollWheelZoom={false}>
        <TileLayer attribution="&copy; OpenStreetMap" url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
        {lat && lon && (
          <Marker position={[lat, lon]}>
            <Popup>{label}<br/>{lat.toFixed(2)}, {lon.toFixed(2)}</Popup>
          </Marker>
        )}
      </MapContainer>
    </div>
  );
}
