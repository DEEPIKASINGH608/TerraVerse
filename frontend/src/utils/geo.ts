export function formatArea(areaSqm?: number): string {
  if (!areaSqm) return 'N/A';
  if (areaSqm >= 10000) {
    return `${(areaSqm / 10000).toFixed(2)} ha`;
  }
  return `${areaSqm.toFixed(2)} m²`;
}

export function getSeverityBadgeClass(severity: string): string {
  switch (severity) {
    case 'critical':
      return 'bg-red-500 text-white';
    case 'high':
      return 'bg-orange-500 text-white';
    case 'medium':
      return 'bg-yellow-500 text-black';
    case 'low':
      return 'bg-blue-500 text-white';
    default:
      return 'bg-gray-400 text-white';
  }
}