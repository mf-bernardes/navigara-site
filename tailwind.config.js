/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
  ],
  theme: {
    // Sobrescreve a configuração do container padrão do Tailwind
    container: {
      center: true,
      padding: '2rem',
      screens: {
        '2xl': '1100px', // Define a largura máxima do container para 1100px
      },
    },
    extend: {
      // Adiciona sua paleta de cores customizada
      colors: {
        'light': '#efeaea',
        'dark': '#340909',
        'accent': {
          'red-dark': '#631f15',
          'red-medium': '#923521',
          'red-light': '#c24c2d',
          // ADICIONE AS NOVAS CORES AQUI
          'blue': '#2b5d8b',
          'blue-light': '#5c85b1',
        },
        'neutral-gray': '#8D8787',
      },
      // Adiciona a fonte 'Poppins' à lista de fontes
      fontFamily: {
        sans: ['Poppins', 'sans-serif'],
      },
    },
  },
  plugins: [],
}