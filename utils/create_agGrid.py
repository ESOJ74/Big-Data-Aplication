import dash_ag_grid as dag


def create_adgrid(id, df):
    
    dashGridOptions={"pagination": False}
    style = {"width": "100%"}
    
    match df.shape[0]:
        case 1|2|3:            
            style["height"] = 200
        case 4|5:
            style["height"] = 280
        case 6|7:
            style["height"] = 360
        case 8|9:
            style["height"] = 400
        case _:
            style["height"] = "100%"
            dashGridOptions={"pagination": True}

    return dag.AgGrid(
                      id=id,
                      className="ag-theme-alpine",
                      columnDefs=[{"headerName": x, "field": x}
                                  for x in df.columns],
                      rowData=df.to_dict("records"),
                    
                      #columnSize="sizeToFit",
                      dashGridOptions=dashGridOptions,
                      style=style,)

"""Allowed arguments: AsyncTransactionsFlushed, accentedSort, aggFuncs, aggregateOnlyChangedColumns, alignedGrids,allowContextMenuWithControlKey, allowDragFromColumnsToolPanel,
 allowShowChangeAfterFilter, alwaysShowHorizontalScroll,alwaysShowVerticalScroll, animateRows, animationQueueEmpty, applyColumnDefOrder, asyncTransactionWaitMillis, autoGroupColumnDef,
autoSizePadding, blockLoadDebounceMillis, bodyScroll, cacheBlockSize, cacheOverflowSize, cacheQuickFilter, cellClicked, cellContextMenu, 
cellDoubleClicked, cellEditingStarted, cellEditingStopped, cellFadeDelay, cellFlashDelay, cellFocused, cellKeyDown, cellKeyPress, cellMouseDown,
cellMouseOut, cellMouseOver, cellStyle, cellValueChanged, chartThemeOverrides, chartThemes, className, clickData, clipboardDeliminator,
colResizeDefault, columnDefs, columnEverythingChanged, columnGroupOpened, columnMoved, columnPinned, columnPivotChanged, columnPivotModeChanged,
columnResized, columnRowGroupChanged, columnSize, columnState, columnTypes, columnValueChanged, columnVisible, componentStateChanged, components,
context, copyHeadersToClipboard, csvExportParams, customChartThemes, dangerously_allow_html, dashGridOptions, data_previous, data_previous_timestamp,
debounceVerticalScrollbar, debug, defaultColDef, defaultColGroupDef, defaultExportParams, detailCellRendererParams, detailRowAutoHeight, detailRowHeight,
displayedColumnsChanged, domLayout, dragStarted, dragStopped, editType, enableAddRows, enableAutoSizeAllColumns, enableAutoSizeAllColumnsSkipHeaders,
enableBrowserTooltips, enableCellChangeFlash, enableCellExpressions, enableCellTextSelection, enableCharts, enableDeleteSelectedRows, enableDeselectAll,
enableEnterpriseModules, enableExportDataAsCsv, enableFillHandle, enableRangeHandle, enableRangeSelection, enableResetColumnState, enableRtl,
enableSelectAll, enableSelectAllFiltered, enableUpdateColumnDefs, ensureDomOrder, enterMovesDown, excelStyles, excludeChildrenWhenTreeDataFiltering,
expandOrCollapseAll, fillHandleDirection, filterChanged, filterModified, firstDataRendered, floatingFiltersHeight, frameworkComponents,
fullWidthCellRenderer, functionsReadOnly, getDetailRequest, getDetailResponse, getRowStyle, getRowsRequest, getRowsResponse, gridColumnsChanged,
gridReady, gridSizeChanged, groupDefaultExpanded, groupHeaderHeight, groupHideOpenParents, groupIncludeFooter, groupIncludeTotalFooter,
groupMultiAutoColumn, groupRemoveLowestSingleChildren, groupRemoveSingleChildren, groupRowInnerRenderer, groupRowRenderer, groupSelectsChildren,
groupSelectsFiltered, groupSuppressAutoColumn, groupSuppressBlankHeader, groupUseEntireRow, headerHeight, hoverData, icons, id, immutableData, 
keepDetailRows, keepDetailRowsCount, layoutInterval, licenseKey, loadingOverlayComponent, loadingOverlayComponentParams, localeText, masterDetail,
maxBlocksInCache, maxConcurrentDatasourceRequests, modelUpdated, multiSortKey, newColumnsLoaded, noRowsOverlayComponent, noRowsOverlayComponentParams,
overlayLoadingTemplate, overlayNoRowsTemplate, paginateChildRows, pagination, paginationAutoPageSize, paginationChanged, paginationPageSize, pasteEnd,
pasteStart, persisted_props, persistence, persistence_type, pinnedBottomRowData, pinnedRowDataChanged, pinnedTopRowData,pivotColumnGroupTotals, pivotGroupHeaderHeight,
pivotHeaderHeight, pivotMode, pivotPanelShow, pivotRowTotals, pivotSuppressAutoColumn, popupParent, preventDefaultOnContextMenu, purgeClosedRowNodes, quickFilterText,
rangeSelectionChanged, rowBuffer, rowClass, rowClassRules, rowClicked, rowData, rowDataChanged, rowDataUpdated, rowDoubleClicked, rowDragEnd, rowDragEnter, rowDragLeave,
rowDragManaged, rowDragMove, rowEditingStarted, rowEditingStopped, rowGroupOpened, rowGroupPanelShow, rowHeight, rowModelType, rowMultiSelectWithClick, rowSelected, rowSelection,
rowStyle, rowValueChanged, scrollbarWidth, selectionChanged, serverSideFilteringAlwaysResets, serverSideSortingAlwaysResets, serverSideStoreType, setRowId, showOpenedGroup, sideBar,
singleClickEdit, skipHeaderOnAutoSize, sortChanged, sortingOrder, statusBar, stopEditingWhenGridLosesFocus, style, suppressAggAtRootLevel, suppressAggFilteredOnly,
suppressAggFuncInHeader, suppressAnimationFrame, suppressAsyncEvents, suppressAutoSize, suppressBrowserResizeObserver, suppressCellSelection, suppressClearOnFillReduction,
suppressClickEdit, suppressColumnMoveAnimation, suppressColumnVirtualisation, suppressContextMenu, suppressCopyRowsToClipboard, suppressCsvExport, suppressDragLeaveHidesColumns,
suppressExcelExport, suppressExpandablePivotGroups, suppressFieldDotNotation, suppressFocusAfterRefresh, suppressHorizontalScroll, suppressLastEmptyLineOnPaste, suppressLoadingOverlay,
suppressMaintainUnsortedOrder, suppressMakeVisibleAfterUnGroup, suppressMaxRenderedRowRestriction, suppressMenuHide, suppressMiddleClickScrolls, suppressModelUpdateAfterUpdateTransaction,
suppressMovableColumns, suppressMoveWhenRowDragging, suppressMultiSort, suppressNoRowsOverlay, suppressPaginationPanel, suppressParentsInRowNodes, suppressPreventDefaultOnMouseWheel,
suppressPropertyNamesCheck, suppressRowClickSelection, suppressRowDeselection, suppressRowDrag, suppressRowHoverHighlight, suppressRowTransform, suppressRowVirtualisation,
suppressScrollOnNewData, suppressTouch, theme, toolPanelVisibleChanged, tooltipMouseTrack, tooltipShowDelay, unSortIcon, valueCache, valueCacheNeverExpires, viewportChanged,
viewportDatasource, viewportRowModelBufferSize, viewportRowModelPageSize, virtualColumnsChanged, virtualRowData, virtualRowRemoved"""