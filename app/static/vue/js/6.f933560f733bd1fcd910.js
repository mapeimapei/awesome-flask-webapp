webpackJsonp([6],{wJoh:function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var a=n("3cXf"),i=n.n(a),r=n("4YfN"),s=n.n(r),c=n("b8UZ"),o={name:"addSingle",data:function(){return{articleList:[],currentPage:1,pageSize:5}},computed:s()({},Object(c.c)(["user"]),{articleList2:function(){var t=(this.currentPage-1)*this.pageSize,e=this.currentPage*this.pageSize;return this.articleList.slice(t,e)}}),filters:{},methods:{deleFn:function(t){var e=this;this.$confirm("确定是否删除?","提示",{confirmButtonText:"确定",cancelButtonText:"取消",type:"warning"}).then(function(){e.deletData(t)}).catch(function(){e.$message({type:"info",message:"已取消删除"})})},deletData:function(t){var e=this,n=this.$loading({lock:!0,background:"rgba(0, 0, 0, 0.5)"}),a={id:t,user_id:this.user.id};this.$axios.post("cms/deleteSingle",i()(a)).then(function(t){n.close(),t&&"20000"===t.resultCode?e.getPosts():e.$notify({message:"删除失败",type:"warning"})}).catch(function(t){n.close(),e.$notify({message:"删除接口报错",type:"warning"})})},editFn:function(t){this.$router.push({path:"addSingle",query:{id:t}})},getPosts:function(){var t=this,e=this.$loading({lock:!0,background:"rgba(0, 0, 0, 0.5)"});this.$axios.get("cms/getPosts").then(function(n){e.close(),n&&"20000"===n.resultCode?t.articleList=n.result:t.$notify({message:"获取文章列表失败。",type:"warning"})}).catch(function(n){e.close(),t.$notify({message:"获取文章列表接口报错。",type:"warning"})})}},mounted:function(){},created:function(){this.getPosts()}},l=n("W5g0"),u=Object(l.a)(o,function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"articleBox fx-f1"},[n("el-table",{staticClass:"articleList",attrs:{data:t.articleList2,border:""}},[n("el-table-column",{attrs:{prop:"name",label:"标题"}}),t._v(" "),n("el-table-column",{attrs:{prop:"user_name",label:"作者",width:"180"}}),t._v(" "),n("el-table-column",{attrs:{prop:"created_at",label:"创建时间",width:"200"},scopedSlots:t._u([{key:"default",fn:function(e){return[n("span",{staticClass:"elli"},[t._v(t._s(e.row.created_at))])]}}])}),t._v(" "),n("el-table-column",{attrs:{label:"操作",width:"200"},scopedSlots:t._u([{key:"default",fn:function(e){return[n("el-button",{attrs:{type:"text"},on:{click:function(n){return t.deleFn(e.row.id)}}},[t._v("删除")]),t._v(" "),n("el-button",{attrs:{type:"text"},on:{click:function(n){return t.editFn(e.row.id)}}},[t._v("编辑")])]}}])})],1),t._v(" "),n("el-pagination",{attrs:{"current-page":t.currentPage,"page-size":t.pageSize,layout:"total, prev, pager, next",total:t.articleList.length},on:{"update:currentPage":function(e){t.currentPage=e},"update:current-page":function(e){t.currentPage=e}}})],1)},[],!1,null,null,null);e.default=u.exports}});
//# sourceMappingURL=6.f933560f733bd1fcd910.js.map