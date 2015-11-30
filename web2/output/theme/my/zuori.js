
  $(document).ready(function() {
  $('#mytable2').dataTable( {
    searching: true,
    paging: true,
    ordering: true,
    orderMulti : true,
    pageLength: 100,
    order: [[ 2, 'asc' ],[ 4, 'asc' ], [8,'desc']],
    columnDefs: [
    {
      targets: [ 4 ],
      orderData: [ 4, 8 ]
    },
    {
      targets: [ 8],
      orderData: [ 8, 4 ]
    },
    {
      targets: [ 1],
      orderData: [ 1, 0 ]
    },
    {
      targets: [ 2],
      orderData: [ 2, 4, 8 ]
    },
    {
      targets: [ 3],
      orderData: [ 3, 4,8 ]
    },
    {
      targets: [ 5],
      orderData: [ 5, 4,8 ]
    },
    {
      targets: [ 6],
      orderData: [ 6, 4,8 ]
    },
    {
      targets: [ 7],
      orderData: [ 7, 4,8 ]
    },
    {
      targets: [ 0 ],
      orderData: [ 0, 1]
    } ],
     columns: [    { type: "html" },    { type: "html" },    { type: "num" },    { type: "num" }, {type:"num"} ,{type:"num"} , {type:"num"}, {type:"num"} , {type:"num"} ,{ type: "html" }]
  } );
} );
