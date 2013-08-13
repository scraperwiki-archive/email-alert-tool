var execSuccess = function(execOutput) {
  $('#submitBtn').removeClass('loading').html('<i class="icon-ok"></i> Saved')
  $('#submitBtn').attr('disabled', false)
  setTimeout(function() {
    $('#submitBtn').html('Save')
  }, 2000)
}

var errorHandler = function(jqXHR, textStatus, errorThrown) {
  console.log("Error! " + jqXHR + textStatus + errorThrown)   
}
 
var insertSavedValues = function() {
  var query = "select value_blob from swvariables where name='recipient';" 
  scraperwiki.tool.sql(query, function(data, textStatus, jqXHR) {
    $('#email').val(data[0]['value_blob']);
  }, errorHandler)

  var query = "select value_blob from swvariables where name='tablename';" 
  scraperwiki.tool.sql(query, function(data, textStatus, jqXHR) {
    $('#tablename').val(data[0]['value_blob'])
  }, errorHandler)
}

var populateForm = function() {
  scraperwiki.sql.meta(function(data) {
    $.each(data.table, function(key, value) {
      $('#tablename').append('<option value="' + key + '">' + key + '</option>')
    })
    insertSavedValues()  
  })
}

var saveForm = function() {
  $(this).attr('disabled', true)  // Disable further clicks.
  $(this).addClass('loading').html('Saving&hellip;')  // Spinny loader.
  var email = scraperwiki.shellEscape($('#email').val())
  var tableName = scraperwiki.shellEscape($('#tablename').val())
  var endpointUrl = scraperwiki.readSettings().source.url + '/sqlite?q=select count(*) from ' + tableName + ';'
  endpointUrl = scraperwiki.shellEscape(endpointUrl)
  scraperwiki.exec('/home/tool/http/update_db.py ' + email + ' ' + endpointUrl + ' '  + tableName, execSuccess)
}
 
$(function() {
  $('#submitBtn').on('click', saveForm)
  populateForm()
})

