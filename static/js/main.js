htmx.on("closeModal", (event) => {
    console.log("I am closing the modal");
    var modalId = event.detail.value
    if (event.detail.value) {
      var myModalEl = document.getElementById(event.detail.value);
    }else {
      var myModalEl = document.getElementById("sg_create_modal");
    }
    var modal = bootstrap.Modal.getInstance(myModalEl)
    // const modal = new bootstrap.Modal(document.getElementById("sg_create_modal"))
    console.log("closeModal",event.detail.value);
    console.log("modal",modal);
    if (modal) {
      console.log("LOGGING MODAL ", modal);
      modal.hide()
    } 
  })