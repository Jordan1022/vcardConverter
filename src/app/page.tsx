import { useState } from 'react';

export default function Home() {
  const [file, setFile] = useState<File | null>(null);

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setFile(event.target.files?.[0] || null);
  };

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    if (!file) return;

    const formData = new FormData();
    formData.append('file', file);

    const response = await fetch('/api/convert', {
      method: 'POST',
      body: formData,
    });

    if (response.ok) {
      const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'vcards.zip';
      document.body.appendChild(a);
      a.click();
      a.remove();
    } else {
      console.error('Failed to convert file');
    }
  };

  return (
    <div>
      <h1>CSV to vCard Converter</h1>
      <form onSubmit={handleSubmit}>
        <input type="file" accept=".csv" onChange={handleFileChange} />
        <button type="submit">Convert</button>
      </form>
    </div>
  );
}