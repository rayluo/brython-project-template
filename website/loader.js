// Loader creates loading html and injects it into the page

function start_loader(message) {
   const loader = document.createElement("div");
    Object.assign(loader, {
      id: 'loading'
    })

    const psychology = document.createElement("div");
    Object.assign(psychology, {
      id: 'psychology',
       className : 'pulsing'
    })

    const loading_icon = document.createElement("i");
    Object.assign(loading_icon, {
      id: 'loading_icon',
       className : 'fa fa-circle-o-notch fa-spin fa-fw'
    })
    psychology.appendChild(loading_icon);

    const loading_message = document.createElement("span");
    Object.assign(loading_message, {
      id: 'loading_message',
    })
    loading_message.innerHTML = message;
    psychology.appendChild(loading_message);

   loader.appendChild(psychology);
   document.body.appendChild(loader);

   console.log(message)

}


function update_loader_message(message) {
    document.getElementById('loading_message').innerHTML = message;
    console.log(message)
}