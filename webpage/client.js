
class Results{
    constructor(data){
        this.labels = data.map(row => row.data); //x axis
        this.counts = data.map(row => row.count); //y axis    
    }
    
}






document.addEventListener('DOMContentLoaded', async () => {
    try {

        const response = await fetch('http://localhost:5000/count');
        const data = await response.json();

        const newdata = new Results(data)

        const ctx = document.getElementById('plot').getContext('2d');
        myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: newdata.labels,
                datasets: [{
                    label: 'Count',
                    data: newdata.counts,
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            },
            maintainAspectRatio: true, // Esto permite cambiar las dimensiones
            responsive: false,
        });
    } catch (error) {
        console.error('Error al cargar los datos del gráfico:', error);
    }
});


async function fetchPlot(value){
    try{
        const response = await fetch('http://localhost:5000/'+value);
        let data = await response.json()
        
        return data
    } catch (error){
        console.error(error)
        return []
    }
};

async function updateChart() {
    
    const value = document.getElementById('select_plot').value;
    const data = await fetchPlot(value);
    const data_test = new Results(data)

    myChart.data.labels = data_test.labels; 
    myChart.data.datasets[0].data = data_test.counts;

    myChart.update();

}






 
    
