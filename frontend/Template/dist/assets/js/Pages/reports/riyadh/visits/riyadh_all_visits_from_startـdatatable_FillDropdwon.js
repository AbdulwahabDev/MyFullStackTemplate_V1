 


function GetSelectSelectedValues_lookups(select_Id) {
  tempList = [];
  for (const element of $(select_Id).find(":selected")) {
    tempList.push(element.value);
  }
  return tempList;
}

function Get_datatableQuery_lookUps() {
  return {
    RAQEB_ENTITY_ID: GetSelectSelectedValues_lookups("#RAQEB_ENTITY_ID"),
    ENTITY_VISIT_ID: GetSelectSelectedValues_lookups("#ENTITY_VISIT_ID"),
    TASK_TYPE_NAME: GetSelectSelectedValues_lookups("#TASK_TYPE_NAME"),
    VISIT_STATUS_NAME: GetSelectSelectedValues_lookups("#VISIT_STATUS_NAME"),
    SECTION_NAME: GetSelectSelectedValues_lookups("#SECTION_NAME"),
    BILL_STATUS: GetSelectSelectedValues_lookups("#BILL_STATUS"),
    BILL_STATUS_NAME: GetSelectSelectedValues_lookups("#BILL_STATUS_NAME"),
    BILL_STATUS_1: GetSelectSelectedValues_lookups("#BILL_STATUS_1"),
    OWNER_ID_TYPE: GetSelectSelectedValues_lookups("#OWNER_ID_TYPE"),
    USER_ID: GetSelectSelectedValues_lookups("#USER_ID"),
    OWNER_ID: GetSelectSelectedValues_lookups("#OWNER_ID"),
    
  };
}

function GetAllOwnerIDs(New_OWNER_ID) {

   
  return new Promise(function (resolve, reject) {
    var settings = {
      url: Tables_host_Url+"/riyadh/raqeb/visits/get_OWNER_ID_list_",
      method: "PUT",
      timeout: 0,
      headers: {
        "Content-Type": "application/json",
      },
      xhrFields: {
        withCredentials: true,
      },
      data: JSON.stringify({OWNER_ID: [New_OWNER_ID]}),
    };
  
    $.ajax(settings)
    .done(function (result) {
       
      
      resolve({'select_result':result,'New_OWNER_ID':New_OWNER_ID})
       
    })
    .fail(function (response) {
     
      })
    .always(function (response) {

    });
  
    
    
  }) 
}


function Get_TASK_TYPE_NAME_Values() {
  return new Promise(function (resolve, reject) {
    var settings = {
      url: Tables_host_Url+"/riyadh/raqeb/visits/get_TASK_TYPE_NAME_list_",
      method: "PUT",
      timeout: 0,
      headers: {
        "Content-Type": "application/json",
      },
      xhrFields: {
        withCredentials: true,
      },
      data: JSON.stringify(Get_datatableQuery_lookUps()),
    };

    $.ajax(settings)
      .done(function (result) {
        if ($("#TASK_TYPE_NAME").find(":selected").length == 0) {
 
          $("#TASK_TYPE_NAME").empty().trigger("change");
          // Append it to the select
          // $('#TASK_TYPE_NAME').append(new Option('الكل', 'ALL', true, true));
          for (const element of result) {
            // Append it to the select
            $("#TASK_TYPE_NAME").append(
              new Option(element, element, false, false)
            );
          }
        }
        // $('#TASK_TYPE_NAME').select2('open');
      })
      .fail(function (response) {})
      .always(function (response) {
        resolve()
      });
  });
}
function Get_VISIT_STATUS_NAME_Values() {
    return new Promise(function (resolve, reject) {
      var settings = {
        url: Tables_host_Url+"/riyadh/raqeb/visits/get_VISIT_STATUS_NAME_list_",
        method: "PUT",
        timeout: 0,
        headers: {
          "Content-Type": "application/json",
        },
        xhrFields: {
          withCredentials: true,
        },
        data: JSON.stringify(Get_datatableQuery_lookUps()),
      };
 
       
    $.ajax(settings)
      .done(function (result) {
         
        if ($("#VISIT_STATUS_NAME").find(":selected").length == 0) { 
          $("#VISIT_STATUS_NAME").empty().trigger("change"); 
          for (const element of result) { 
            
            $("#VISIT_STATUS_NAME").append(
              new Option(element, element, false, false)
            );
          }
        }
        // $('#VISIT_STATUS_NAME').select2('open');
      })
      .fail(function (response) {})
      .always(function (response) {
         
        resolve()});
  });
}
function Get_SECTION_NAME_Values() {
  return new Promise(function (resolve, reject) {

    var settings = {
      url: Tables_host_Url+"/riyadh/raqeb/visits/get_SECTION_NAME_list_",
      method: "PUT",
      timeout: 0,
      headers: {
        "Content-Type": "application/json",
      },
      xhrFields: {
        withCredentials: true,
      },
      data: JSON.stringify(Get_datatableQuery_lookUps()),
    };

 

    $.ajax(settings)
      .done(function (result) {
        if ($("#SECTION_NAME").find(":selected").length == 0) {
 
          $("#SECTION_NAME").empty().trigger("change");
          // Append it to the select
          // $('#SECTION_NAME').append(new Option('الكل', 'ALL', true, true));
          for (const element of result) {
            // Append it to the select
            $("#SECTION_NAME").append(
              new Option(element, element, false, false)
            );
          }
        }
        // $('#SECTION_NAME').select2('open');
      })
      .fail(function (response) {})
      .always(function (response) {
        resolve()});
  });
}
function Get_BILL_STATUS_NAME_Values() {
  return new Promise(function (resolve, reject) {

    var settings = {
      url: Tables_host_Url+"/riyadh/raqeb/visits/get_BILL_STATUS_NAME_list_",
      method: "PUT",
      timeout: 0,
      headers: {
        "Content-Type": "application/json",
      },
      xhrFields: {
        withCredentials: true,
      },
      data: JSON.stringify(Get_datatableQuery_lookUps()),
    };
      

    $.ajax(settings)
      .done(function (result) {
        if ($("#BILL_STATUS_NAME").find(":selected").length == 0) {
 
          $("#BILL_STATUS_NAME").empty().trigger("change");
          // Append it to the select
          // $('#BILL_STATUS_NAME').append(new Option('الكل', 'ALL', true, true));
          for (const element of result) {
            // Append it to the select
            $("#BILL_STATUS_NAME").append(
              new Option(element, element, false, false)
            );
          }
        }
        // $('#BILL_STATUS_NAME').select2('open');
      })
      .fail(function (response) {})
      .always(function (response) {
        resolve()});
  });
}
function Get_BILL_STATUS_1_Values() {
  return new Promise(function (resolve, reject) {

    var settings = {
      url: Tables_host_Url+"/riyadh/raqeb/visits/get_BILL_STATUS_1_list_",
      method: "PUT",
      timeout: 0,
      headers: {
        "Content-Type": "application/json",
      },
      xhrFields: {
        withCredentials: true,
      },
      data: JSON.stringify(Get_datatableQuery_lookUps()),
    };
      
 

    $.ajax(settings)
      .done(function (result) {
        if ($("#BILL_STATUS_1").find(":selected").length == 0) {
 
          $("#BILL_STATUS_1").empty().trigger("change");
          // Append it to the select
          // $('#BILL_STATUS_1').append(new Option('الكل', 'ALL', true, true));
          for (const element of result) {
            // Append it to the select
            $("#BILL_STATUS_1").append(
              new Option(element, element, false, false)
            );
          }
        }
        // $('#BILL_STATUS_1').select2('open');
      })
      .fail(function (response) {})
      .always(function (response) {
        resolve()});
  });
}
function Get_OWNER_ID_TYPE_Values() {
  return new Promise(function (resolve, reject) {


    var settings = {
      url: Tables_host_Url+"/riyadh/raqeb/visits/get_OWNER_ID_TYPE_list_",
      method: "PUT",
      timeout: 0,
      headers: {
        "Content-Type": "application/json",
      },
      xhrFields: {
        withCredentials: true,
      },
      data: JSON.stringify(Get_datatableQuery_lookUps()),
    };
      
 
 

    $.ajax(settings)
      .done(function (result) {
         if ($("#OWNER_ID_TYPE").find(":selected").length == 0) {
 
          $("#OWNER_ID_TYPE").empty().trigger("change");
          // Append it to the select
          // $('#OWNER_ID_TYPE').append(new Option('الكل', 'ALL', true, true));
          for (const element of result) {
            // Append it to the select
            $("#OWNER_ID_TYPE").append(
              new Option(element, element, false, false)
            );
          }
        }
        // $('#OWNER_ID_TYPE').select2('open');
      })
      .fail(function (response) {
      }
        )
      .always(function (response) {
        resolve()
      });
  });
}
function Get_USER_ID_Values() {
  return new Promise(function (resolve, reject) {
  
    var settings = {
      url: Tables_host_Url+"/riyadh/raqeb/visits/get_USER_ID_list_",
      method: "PUT",
      timeout: 0,
      headers: {
        "Content-Type": "application/json",
      },
      xhrFields: {
        withCredentials: true,
      },
      data: JSON.stringify(Get_datatableQuery_lookUps()),
    }; 
    $.ajax(settings)
      .done(function (result) {
        if ($("#USER_ID").find(":selected").length == 0) {
 
          $("#USER_ID").empty().trigger("change");
          // Append it to the select
          // $('#OWNER_ID_TYPE').append(new Option('الكل', 'ALL', true, true));
          for (const element of result) {
            // Append it to the select
            $("#USER_ID").append(
              new Option(element, element, false, false)
            );
          }
        } 
      })
      .fail(function (response) {})
      .always(function (response) {
        resolve()
      });
  });
}
 
 

function createTag_for_select() {
  
   
  $("#OWNER_ID").select2({
    multiple: true,
    tokenSeparators: [',', ' '], 
    placeholder: 'أكتب رقم الهوية ',
    createTag: function (params) {
        
            var term = $.trim(params.term);
            if (term === '' || term.length < 5) {
                return null;
            }
            else{

               
              var settings = {
                url: Tables_host_Url+"/riyadh/raqeb/visits/get_OWNER_ID_list_",
                method: "PUT",
                timeout: 0,
                headers: {
                  "Content-Type": "application/json",
                },
                xhrFields: {
                  withCredentials: true,
                },
                data: JSON.stringify({OWNER_ID: [term]}),
              };
            
              $.ajax(settings)
              .done(function (result) {
                
                console.log('pass result');
                console.log(result);


                $('#OWNER_ID').append($('<option>', { 
                  value: term,
                  text : term 
                  })).select2({
                    multiple: true,
                    tokenSeparators: [',', ' '], 
                    placeholder: 'أكتب رقم الهوية ',
                    createTag: function (params) {
                        
                            var term = $.trim(params.term);
                            if (term === '' || term.length < 5) {
                                return null;
                            }
                            else{
                
                               
                              var settings = {
                                url: Tables_host_Url+"/riyadh/raqeb/visits/get_OWNER_ID_list_",
                                method: "PUT",
                                timeout: 0,
                                headers: {
                                  "Content-Type": "application/json",
                                },
                                xhrFields: {
                                  withCredentials: true,
                                },
                                data: JSON.stringify({OWNER_ID: [term]}),
                              };
                            
                              $.ajax(settings)
                              .done(function (result) {
                                
                                console.log('pass result');
                                console.log(result);
                                
                                
                                
                                $('#OWNER_ID').append($('<option>', { 
                                  value: term,
                                  text : term 
                                  }));
                 
                                 
                              })
                              .fail(function (response) {
                                
                                console.log('fail result');
                                console.log(response);
                                })
                              .always(function (response) {
                          
                              });  
                            }
                            return null;
                             
                            
                        },
                        tags: true
                    });
 
                 
              })
              .fail(function (response) {
                
                console.log('fail result');
                console.log(response);
                })
              .always(function (response) {
          
              });  
            }
            return null;
             
            
        },
        tags: true
    });



}

// promises = [];
// promises.push(
//   Get_TASK_TYPE_NAME_Values(),
//   Get_VISIT_STATUS_NAME_Values(),
//   Get_SECTION_NAME_Values(), 
//   Get_BILL_STATUS_NAME_Values(),
//   Get_BILL_STATUS_1_Values(),
//   Get_OWNER_ID_TYPE_Values()
//  );
// Promise.all(promises).then(() => { 
//   $(".form-select").select2({
//     tags: true,
//     tokenSeparators: [',', ' ']
//   })
// });

// function OnSelectChange(e) {
//   promises = [];
   
//   promises.push(
//     // Get_TASK_TYPE_NAME_Values(),
//     // Get_VISIT_STATUS_NAME_Values(),
//     // Get_SECTION_NAME_Values(),
//     // Get_BILL_STATUS_Values(),
//     // Get_BILL_STATUS_NAME_Values(),
//     // Get_BILL_STATUS_1_Values(),
//     // Get_OWNER_ID_TYPE_Values()
//   );
//   Promise.all(promises).then(() => {
//     // jQuery(document).ready(function () { 
//     // });
//   });

//   // Promise.all(promises).then(() => {
//   //   $('#kt_search').click()
//   // });
// }

// $("#TASK_TYPE_NAME,#VISIT_STATUS_NAME").on("select2:unselecting", function (e) {
//   OnSelectChange(e);
// });

// $("#TASK_TYPE_NAME,#VISIT_STATUS_NAME").on("select2:select", function (e) {
//   OnSelectChange(e);
// });

 
 