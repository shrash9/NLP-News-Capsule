// const form = document.querySelector('form');
// const summary = document.querySelector('.summary');

// form.addEventListener('submit', async (event) => {
//   event.preventDefault();
//   summary.innerHTML = 'Loading...';

//   const text = form.text.value;
//   const type = form.type.value;

  
//   const response = await fetch(`/${type}`, {
//     method: 'POST',
//     headers: {
//       'Content-Type': 'application/json'
//     },
//     body: JSON.stringify({ text })
//   });


//   const data = await response.json();
//   if (response.ok) {
//     summary.innerHTML = data.summary;
//   } else {
//     summary.innerHTML = data.error;
//   }
// });