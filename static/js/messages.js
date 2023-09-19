    const toastOptions = { delay: 20000 
    }
    function createToast(message) {
        console.log("HELLLOo");
        // console.log("hello log", message);
        // console.log("message  Tags", message.tags);
        const element = htmx.find("[data-toast-template]").cloneNode(true)
        delete element.dataset.toastTemplate
        element.className += " " + message.tags
        htmx.find(element, "[data-toast-body]").innerHTML = message.message
        htmx.find("[data-toast-container]").appendChild(element)
        const toast = new bootstrap.Toast(element, toastOptions)
        toast.show()
      }

      htmx.on("messages", (event) => {
        console.log("MEssage received");
        event.detail.value.forEach(createToast)
      })

      toastr.options = {
        "closeButton": true,
        "debug": true,
        "newestOnTop": true,
        "progressBar": true,
        "positionClass": "toastr-top-right",
        "preventDuplicates": true,
        "onclick": null,
        "showDuration": "300",
        "hideDuration": "1000",
        "timeOut": "5000",
        "extendedTimeOut": "1000",
        "showEasing": "swing",
        "hideEasing": "linear",
        "showMethod": "fadeIn",
        "hideMethod": "fadeOut"
      };
    htmx.findAll(".toast:not([data-toast-template])").forEach((element) => {
    const toast = new bootstrap.Toast(element, toastOptions)
    console.log("HELLLOo");

    toast.show()
  })


