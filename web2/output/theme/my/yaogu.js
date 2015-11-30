
  $(document).ready(function() {
  $('#mytable1').dataTable( {
    searching: true,
    paging: true,
    ordering: true,
    orderMulti : true,
    pageLength: 100,
    order: [[ 2, 'desc' ], [6,'desc']],
    columnDefs: [
    {
      targets: [ 2 ],
      orderData: [ 2, 6 ]
    },
    {
      targets: [ 3 ],
      orderData: [ 3, 2,6 ]  //如果第二列进行排序，有相同数据则按照第一列顺序排列
    },
    {
      targets: [ 4 ],
      orderData: [ 4, 2,6 ]
    },
    {
      targets: [ 5],
      orderData: [ 5, 2, 6 ]
    },
    {
      targets: [ 6],
      orderData: [ 6, 2,3,4,5 ]
    },
    {
      targets: [ 0 ],
      orderData: [ 0, 1]
    } ],
     columns: [    { type: "html" },    { type: "html" },    { type: "num" },    { type: "num" }, {type:"num"} ,{type:"num"} , {type:"num"} ,    { type: "html" }]
  } );
} );
