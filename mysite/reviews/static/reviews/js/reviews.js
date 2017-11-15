$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-review .modal-content").html("");
        $("#modal-review").modal("show");
      },
      success: function (data) {
        $("#modal-review .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#review-table tbody").html(data.html_review_list);
          $("#modal-review").modal("hide");
        }
        else {
          $("#modal-review .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create review
  $(".js-create-review").click(loadForm);
  $("#modal-review").on("submit", ".js-review-create-form", saveForm);

  // Update review
  $("#review-table").on("click", ".js-update-review", loadForm);
  $("#modal-review").on("submit", ".js-review-update-form", saveForm);

  // Delete review
  $("#review-table").on("click", ".js-delete-review", loadForm);
  $("#modal-review").on("submit", ".js-review-delete-form", saveForm);
  
  // Search review
  $(".js-search-review").click(loadForm);
  $("#modal_review").on("submit", ".js-review-search-form", saveForm);
});
