import React, { useState } from 'react';

// Este es el componente principal de la aplicación visual en React
function App(): JSX.Element {
    // Estados para manejar los datos de la interfaz
    const [videoFile, setVideoFile] = useState<File | null>(null);
    const [prompt, setPrompt] = useState<string>('');
    const [resultVideoUrl, setResultVideoUrl] = useState<string | null>(null);
    const [isLoading, setIsLoading] = useState<boolean>(false);

    // Función que se ejecutaría al presionar el botón "Generar"
    const handleGenerateClick = () => {
        if (!videoFile || !prompt) {
            alert('Por favor, suba un video y escriba un prompt.');
            return;
        }
        setIsLoading(true);
        console.log('Iniciando proceso de animación...');

        // Lógica conceptual para enviar los datos al Backend (a implementar en el futuro)
        // const formData = new FormData();
        // formData.append('video', videoFile);
        // formData.append('prompt', prompt);
        // fetch('/process-video', { method: 'POST', body: formData })
        //   .then(response => response.json())
        //   .then(data => {
        //      setResultVideoUrl(data.videoUrl); 
        //      setIsLoading(false);
        //   });
    };

    return (
        <div className="App">
            <header>
                <h1>Plataforma "Kenpo Avatar"</h1>
                <p>Dirigida por Sergio Valenzuela</p>
            </header>

            <main>
                <section id="uploader-section">
                    <h2>Paso 1: Subir Video de Origen</h2>
                    <input 
                        type="file" 
                        accept="video/mp4,video/quicktime" 
                        onChange={(e) => setVideoFile(e.target.files ? e.target.files[0] : null)}
                    />
                </section>

                <section id="prompt-section">
                    <h2>Paso 2: Describir la Dirección Artística</h2>
                    <textarea 
                        rows={10}
                        style={{ width: '80%', padding: '10px' }}
                        placeholder="Pegue aquí el prompt de dirección artística..."
                        value={prompt}
                        onChange={(e) => setPrompt(e.target.value)}
                    />
                </section>

                <section id="action-section">
                    <button onClick={handleGenerateClick} disabled={isLoading} style={{ padding: '10px 20px', fontSize: '16px' }}>
                        {isLoading ? 'Generando...' : 'Generar Animación'}
                    </button>
                </section>

                <section id="result-section">
                    <h2>Resultado:</h2>
                    <div id="video-output-container">
                        {resultVideoUrl && (
                            <video controls src={resultVideoUrl} width="600"></video>
                        )}
                    </div>
                </section>
            </main>
        </div>
    );
}

export default App;
